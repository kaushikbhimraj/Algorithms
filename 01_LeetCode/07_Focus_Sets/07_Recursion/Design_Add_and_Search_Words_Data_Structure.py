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


# Not able to figure out the logic for when there is a '.' in the end of the search string. 
class Node:
    def __init__(self):
        self.next = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        node = self.root
        for s in word:
            if (not node.next or s not in node.next):
                node.next[s] = Node()
            node = node.next[s]
        
        node.next[""] = Node()
        node.next[""].isEnd = True

    def search(self, word: str) -> bool:        
        node = self.root
        return self.searchHelper(node, word, 0)
    
    def searchHelper(self, node, word, idx):
        if (idx >= len(word) or node.isEnd):
            return True
        
        if (word[idx] != "."):
            if (word[idx] not in node.next):
                return False
            return self.searchHelper(node.next[word[idx]], word, idx+1)
        else:
            for key in node.next:
                return self.searchHelper(node.next[key], word, idx+1)
        return False
            