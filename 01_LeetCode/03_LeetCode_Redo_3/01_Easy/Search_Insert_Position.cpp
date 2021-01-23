/*
Given a sorted array of distinct integers and a target value, return the index if the 
target is found. If not, return the index where it would be if it were inserted in order.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Example 4:
Input: nums = [1,3,5,6], target = 0
Output: 0

Example 5:
Input: nums = [1], target = 0
Output: 0
 
Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104

nums contains distinct values sorted in ascending order.
-104 <= target <= 104

T: O(log n); S: O(1)
*/

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        if (target == 0) return 0;
        
        int left = 0;
        int right = nums.size()-1;
        
        while (left <= right){
            int mid = left + (int) ((right - left)/2);
            
            if (nums.at(mid) == target) return mid;
            else if (nums.at(mid) < target) left = mid + 1;
            else right = mid - 1;
        }
        
        return left;
    }
};