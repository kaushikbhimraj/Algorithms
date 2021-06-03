"""
# 211
Design a data structure that supports adding new words and finding if a string matches any 
previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or 
false otherwise. word may contain dots '.' where dots can be matched with any letter.
"""


class Node:
    def __init__(self):
        self.next = {}
        self.isEnd = False

class WordDictionary:
    def __init__(self):
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        node = self.root
        for s in word:
            if (not node.next or s not in node.next):
                node.next[s] = Node()
            node = node.next[s]
        node.isEnd = True

    def search(self, word: str) -> bool:        
        node = self.root
        self.res = False
        self.searchHelper(node, word)
        return self.res
    
    def searchHelper(self, node, word):
        # Termiantion conditions
        if (not word): 
            if (node.isEnd):
                self.res = True
            return

        if (word[0] == "."):
            for n in node.next.values():
                self.searchHelper(n, word[1:])
        else:
            if (word[0] not in node.next):
                return
            self.searchHelper(node.next[word[0]], word[1:])
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
            