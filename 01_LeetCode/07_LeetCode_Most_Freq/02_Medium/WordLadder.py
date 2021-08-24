"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length 
of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

# T: O(M^2 x N): M - length of each word, N - total number of words in word list.

from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0
        
        # Create a dictionary
        n = len(beginWord)
        adj = defaultdict(list)
        for word in wordList:
            for i in range(n):
                adj[word[:i] + "*" + word[i+1:]].append(word)
        
        # Implement a BFS
        queue = [(beginWord,1)]
        visited = {beginWord: True}
        
        while queue:
            currWord, level = queue.pop(0)
            for i in range(n):
                temp = currWord[:i] + "*" + currWord[i+1:]
                for word in adj[temp]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                adj[temp] = []
        return 0