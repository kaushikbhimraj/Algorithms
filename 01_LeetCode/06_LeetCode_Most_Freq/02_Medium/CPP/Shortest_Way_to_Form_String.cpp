/*
From any string, we can form a subsequence of that string by deleting some number of characters 
(possibly no deletions).

Given two strings source and target, return the minimum number of subsequences of source such that 
their concatenation equals target. If the task is impossible, return -1.

 

Example 1:

Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source 
"abc".
Example 2:

Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due 
to the character "d" in target string.
Example 3:

Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
 

Constraints:

Both the source and target strings consist of only lowercase English letters from "a"-"z".
The lengths of source and target string are between 1 and 1000.
*/

class Solution {
public:
    
    // Two pointers: 1 for source and 1 for target
    // For each character in target, check if it exists in source. 
    // If so, increment both pointers to check if the next characters match as well. 
    // If it doesn't, match increment only the source pointer. 
    // In the end, if the character in target doesn't match anything in source return -1.
    // Use a flag to understand if we have a match. 
    // Each iteration update the counter. 
    
    int shortestWay(string source, string target) {
        int tar = 0;
        int num = 0;
        while (tar < target.length()){
            int src = 0;
            int flag = false; 
            while (src < source.length() && tar < target.length()){
                if (source.at(src) == target.at(tar)){
                    src++;
                    tar++;
                    flag = true;
                }
                else{
                    src++;
                }
            }
            if (flag){
                num++;
            }else{
                return -1;
            }
        }
        return num;
    }
};