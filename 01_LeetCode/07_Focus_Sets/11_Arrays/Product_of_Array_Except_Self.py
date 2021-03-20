"""
Given an integer array `nums`, return *an array* `answer` *such that* `answer[i]` 
*is equal to the product of all the elements of* `nums` *except* `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

**Example 1:**

```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

```

**Example 2:**

```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

```

**Constraints:**

- `2 <= nums.length <= 105`
- `30 <= nums[i] <= 30`
- The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

**Follow up:**

- Could you solve it in `O(n)` time complexity and without using division?
- Could you solve it with `O(1)` constant space complexity? (The output array **does not** 
count as extra space for space complexity analysis.)
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1] * len(nums)
        r = [1] * len(nums)
        
        for i in range(1, len(nums)):
            l[i] = nums[i-1] * l[i-1]
        
        for j in range(len(nums)-2, -1, -1):
            r[j] = nums[j+1] * r[j+1]
            
        for i in range(len(nums)):
            nums[i] = l[i] * r[i]
        
        return nums