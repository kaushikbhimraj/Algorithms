"""
Given an array of integers and an integer k, you need to find the total number 
of continuous sub-arrays whose sum equals to k.
k = 7
nums = [3, 4, 7, 2, -3, 1, 4, 2]
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # need 1 dictionary, 2 variables. 
        cache = dict()
        cache[0] = 1
        
        # cache key: sums of all elements in array until ith position
        # cache value: value + 1 if exists else 1
        sums = 0
        count = 0
        
        # count will update with value in cachce if key -> sums and k exists.
        # insert value in cachce with value @ sums + 1 
        # if value does not exist in cache, insert key as sums and value as 1.
        for i in range(len(nums)):
            sums += nums[i]
            count += cache.get(sums-k, 0) 
            cache[sums] = cache.get(sums, 0) + 1
        
        return count