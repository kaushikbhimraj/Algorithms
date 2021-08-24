"""
Given a list of accounts where each element accounts[i] is a list of strings, where the first element 
accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common 
email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people 
could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, 
and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

 

Example 1:

Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],
["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Example 2:

Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],
["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],
["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
 
Constraints:

1 <= accounts.length <= 1000
2 <= accounts[i].length <= 10
1 <= accounts[i][j] <= 30
accounts[i][0] consists of English letters.
accounts[i][j] (for j > 0) is a valid email.

"""

# Classic union find data structure. 
class Disjoint:
    def __init__(self):
        self.p = range(100001)
        
    # Find executed using recursion.
    def find(self, x):
        if (self.p[x] != x):
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    # Simply find the x and y in self.p and associate them as key: value pair. 
    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)

class Solution:
    def accountsMerge(self, accounts):
        dis = Disjoint()
        email_name = {}
        email_pos = {}
        
        i = 0
        for account in accounts:
            name = account[0]
            
            for email in account[1:]:
                email_name[email] = name
                
                if email not in email_pos:
                    email_pos[email] = i
                    i += 1
                dis.union(email_pos[account[1]], email_pos[email])
        
        # MOST TRICKY PART.
        ans = defaultdict(list)
        
        # Based on the keys in email_name
        # find the position of each email, append the email to the array the index position in ans. 
        for email in email_name:
            ans[dis.find(email_pos[email])].append(email)
        
        # For each sub-array contained in ans, sort it and then, add the name in front
        # (get the name from email_name and use the first email from each sub-array 
        #  to find the name in email_name dictionary.)
        return [[email_name[v[0]]] + sorted(v) for v in ans.values()]