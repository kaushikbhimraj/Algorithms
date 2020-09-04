"""
Input 1:
["joe","joe","joe","james","james","james","james","mary","mary","mary"]
[1,2,3,4,5,6,7,8,9,10]
["home","about","career","home","cart","maps","home","home","about","career"]

Input 2: 
["u1","u1","u1","u2","u2","u2"]
[1,2,3,4,5,6]
["a","b","c","a","b","a"]
"""

from itertools import combinations
from collections import defaultdict

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        # Create an array with tuples of (timestamp, username, website) and sort it. 
        packed_tuples = zip(timestamp, username, website)
        packed_tuples = sorted(packed_tuples)
        
        # Create a dictionary to store a user -> [website1, website2, website3, ...]
        # This will be easier to search in the longer run. 
        users = defaultdict(list)
        for timeStamp, userName, webSite in packed_tuples:
        	users[userName].append(webSite)
        
        # Create another dictionary to count number of repetitions in the website sets. 
        # First create all possible sets of 3 from a user[userName] -> [website1, website2, website3, ...]
        counter = defaultdict(int)
        for websites in users.values():
            combos = set(combinations(websites, 3))
            for combo in combos:
            	counter[combo] += 1
                    
        sorted_combos = sorted(counter, key=lambda x: (counter[x],x), reverse=True)
        return sorted_combos[0]