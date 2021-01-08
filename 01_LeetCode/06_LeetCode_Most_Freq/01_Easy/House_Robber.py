# Time:  O(n)
# Space: O(n)

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # Create dp for keep track of max money. 
        # If n = 1, you are at the beginning, so dp[n] = nums[n]
        # If n = 2, consider the max of two values max(nums[n], nums[n-1])
        # If n = 3, consider the max the below two, 
        #      - consider max(two previous houses)
        #      - consider sum of current house and the money sum until n-2 houses.
        # Simply return the last value for maximum sum. 
        dp = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                dp[i] = nums[i]
            elif i == 1:
                dp[i] = max(nums[i], nums[i-1])
            else:
                dp[i] = max(nums[i] + dp[i-2], max(dp[i-1], dp[i-2]))
        return dp[-1]