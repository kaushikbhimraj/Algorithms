"""
Given an array of integers nums and an integer limit, return the size of the longest 
non-empty subarray such that the absolute difference between any two elements of this 
subarray is less than or equal to limit.

Example 1:
Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.

Example 2:
Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.

Example 3:
Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= limit <= 10^9
"""

# Logic can be divided into three parts. 
#   - Divide array into subarray
#   - Find the min, max from subarray and check if diff <= limit
#   - Store the subarray with max length that has diff <= limit

class Solution:
    # Hit TLE!! :(
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        s = len(nums)
        count = 1
        for i in range(s):
            temp = 0
            for j in range(i+1, s+1):
                mx, mn = self.helper(nums[i:j])
                
                if (mx - mn) <= limit:
                    temp = len(nums[i:j])
                    count = max(count, temp)
                
        return count
                
    
    def helper(self, arr):
        mx = mn = arr[0]
        for i in range(1, len(arr)):
            if mn > arr[i]:
                mn = arr[i]
            if mx < arr[i]:
                mx = arr[i]
            
        return mx, mn