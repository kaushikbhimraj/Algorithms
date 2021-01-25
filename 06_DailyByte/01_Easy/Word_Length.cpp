/*
LC.58 - Length of Last Word

Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5

Example 2:
Input: s = " "
Output: 0
 
Constraints:
1 <= s.length <= 104
s consists of only English letters and spaces ' '.

T: O(n); S: O(1)
*/
class Solution {
public:
    int lengthOfLastWord(string s) {
        int count = 0;
        int right = s.length()-1;
        bool isWord = false;
        

        // Begin from last. 
        // See if there is there spaces after the last word, this would throw logic off. 
        // Have a flag to indicate all initial spaces have been skipped. 
        while (right >= 0){
            if (s[right] == ' ' && isWord) return count;
            if (s[right] == ' ' && !isWord) {
                right--;
            }
            else {
                isWord = true;          // => Most important step!
                count++;
                right--;
            }
        }
        return count;
    }
};