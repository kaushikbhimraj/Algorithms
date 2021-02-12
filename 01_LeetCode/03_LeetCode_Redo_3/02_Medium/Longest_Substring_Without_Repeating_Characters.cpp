#include <iostream>
#include <string>
#include <map>

class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {
        if (s.length() == 0) return 0;
        std::map<char, int>locations;
        std::map<char, int>::iterator val;
        int i = 0, j = 0;
        int size = 0;

        while (j < s.length()){
            char temp = s[j];
            val = locations.find(temp);
            if (val != locations.end() && i <= locations[temp]){
                i = locations[temp] + 1;
            }
            locations[temp] = j;
            int len = j - i + 1;
            size = (size < len) ? len : size;
            j++;
        }
        return size;
    }
};