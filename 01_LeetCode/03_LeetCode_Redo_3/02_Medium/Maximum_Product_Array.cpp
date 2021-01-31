#include <iostream>
#include <vector>
#include <algorithm>

class Solution {
public:
    int m = std::min({2,3,4,5});
    int maxProduct(std::vector<int>& nums) {
        int mx = nums[0];
        int mn = nums[0];
        int result = mx;
        
        for (int i=1; i < nums.size(); i++){
            int temp = std::max({mx*nums[i], mn*nums[i], nums[i]});
            mn = std::min({mn*nums[i], mx*nums[i], nums[i]});
            mx = temp;
            result = std::max({mx, mn, result});
        }
        
        return result;
    }
};