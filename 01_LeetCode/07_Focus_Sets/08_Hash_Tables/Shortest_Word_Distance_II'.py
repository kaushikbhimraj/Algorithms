"""
Design a data structure that will be initialized with a string array, and then it should answer queries of the 
shortest distance between two different strings from the array.

Implement the WordDistance class:

WordDistance(String[] wordsDict) initializes the object with the strings array wordsDict.
int shortest(String word1, String word2) returns the shortest distance between word1 and word2 in the array wordsDict.
 
Example 1:
Input
["WordDistance", "shortest", "shortest"]
[[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
Output
[null, 3, 1]

Explanation
WordDistance wordDistance = new WordDistance(["practice", "makes", "perfect", "coding", "makes"]);
wordDistance.shortest("coding", "practice"); // return 3
wordDistance.shortest("makes", "coding");    // return 1
 
Constraints:

1 <= wordsDict.length <= 3 * 104
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
word1 != word2
At most 5000 calls will be made to shortest.
"""
class WordDistance:
    
    # Object initalization will create a dictionary of words and 
    # their location in the given array. 
    def __init__(self, wordsDict: List[str]):
        self.wrd = {}
        for pos, word in enumerate(wordsDict):
            if word in self.wrd:
                self.wrd[word].append(pos)
            else:
                self.wrd[word] = [pos]

    # Main algorithm is to find the minimum distance between the two words. 
    def shortest(self, word1: str, word2: str) -> int:
        dist1 = self.wrd[word1]
        dist2 = self.wrd[word2]
        ans = float('inf')
        for i in dist1:
            for j in dist2:
                ans = min(ans, abs(i-j))
        return ans

    def shortest(self, word1: str, word2: str) -> int:
        dist1 = self.wrd[word1]
        dist2 = self.wrd[word2]
        ans = float('inf')
        l1, l2 = 0, 0

        while (l1 < len(dist1) and l2 < len(dist2)):
            ans = min(ans, abs(dist1[l1] - dist2[l2]))
            if (dist1[l1] < dist2[l2]):
                l1 += 1
            else:
                l2 += 1
        return ans

    # Comparing the locations of two strings in the word dictionary, 
    # When one position is smaller that the other increment pointer for the smaller.
    # Continue this until you reach the end of the shortest array. 
    def shortest(self, word1: str, word2: str) -> int:
        dist1 = self.wrd[word1]
        dist2 = self.wrd[word2]
        l1, l2 = 0, 0
        ans = float('inf')

        while (l1 < len(dist1) and l2 < len(dist2)):
            ans = min(ans, abs(dist1[l1] - dist2[l2]))
            if (dist1[l1] < dist2[l2]):
                l1 += 1
            else:
                l2 += 1
        return ans        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)

# Ok Bava, that sounds good. I will hold for further instructions. Please do let me know if I can support in any way.  