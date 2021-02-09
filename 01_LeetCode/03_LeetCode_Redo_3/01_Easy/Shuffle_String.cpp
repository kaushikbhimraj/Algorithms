#include <iostream>
#include <vector>
#include <string>

class Solution {
public:
    string restoreString(std::string s, std::vector<int>& indices) {
        int n = indices.size();
        std::vector<char> temp(n);
        std::string output = "";

        for (int i=0; i < n; i++){
            temp[indices[i]] = s.at(i);
        }
        for (int i=0; i < temp.size(); i++){
            output += temp[i];
        }
        
        return output;
    }
};