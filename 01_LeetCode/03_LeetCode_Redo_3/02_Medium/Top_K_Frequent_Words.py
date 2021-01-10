"""
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have 
the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
with the number of occurrence being 4, 3, 2 and 1 respectively.

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.
"""

from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Create a word count dictionary T:O(n); S:O(n)
        word_count = {}
        for word in words:
            if (word in word_count):
                word_count[word] += 1
            else:
                word_count[word] = 1
        
        # Create a heap and return the kth top elements. T:O(nlogn); S:O(n) 
        top_elements = []
        for key in word_count.keys():
            heappush(top_elements, (-word_count[key], key))
        
        # Pop values from list and append to output array. T:O(n); S:O(n)
        res = []
        while (k > 0):
            popped = heappop(top_elements)
            res.append(popped[1])
            k -= 1
        return res