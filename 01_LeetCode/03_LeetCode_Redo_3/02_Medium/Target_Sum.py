"""
You are given a list of non-negative integers, a1, a2, ..., an and target value S. 
Now you have 2 symbols + and -. 
For each integer, you should choose one from + and - as its new symbol. 

Find out how many ways to assign symbols to make sum of integers equal to target S. 
"""

class Solution:
	# Brute force method. 
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.count = 0
        self.helper(nums, 0, 0, S)
        return self.count

    """
    Recursion Tree
    								      0
    					0+1	    			                 0-1
    		 0+1+1             0+1-1 	           0-1+1            0-1-1
         0+1+1   0+1+1-1  0+1-1+1  0+1-1-1   0-1+1+1  0-1+1-1   0-1-1+1  0-1-1-1
	
	Sum from above tree

	         							 0
	         					1	              -1
	         			   2        0         0        -2
	         			3     1   1   -1    1   -1   -1   -3  
	"""

    # i == len(nums) is checked to make sure the pointer is not going out of bound. 
    # If we have reach length, check if the running sum equals the target value. 
    # else, run the recursion. 
    def helper(self, nums, i, rsum, tar):
        if (i == len(nums)):
            if (rsum == tar):
                self.count += 1
                return 
        else:
            self.helper(nums, i+1, rsum + nums[i], tar)
            self.helper(nums, i+1, rsum - nums[i], tar)
        return

    # Above method can be optimized using memoization. 
    def findTargetSumWays_memoization(self, nums: List[int], S: int) -> int:
        self.ways = {}
        return self.helper_memo(nums, 0, 0, S)
    
    # Memoization is implemented using hash maps where the (running sum, index) together become the key and value is the count. 
    def helper_memoization(self, nums, i, rsum, tar):
        if (i == len(nums)):
            if (rsum == tar):
                return 1
            else:
                return 0
        
        else:
            if (rsum, i) in self.ways:
                return self.ways[(rsum, i)]
            
            else:
                states_with_plus = self.helper_memoization(nums, i+1, rsum+nums[i], tar)
                states_with_minus = self.helper_memoization(nums, i+1, rsum-nums[i], tar)
                
                self.ways[(rsum, i)] = states_with_plus + states_with_minus
                return self.ways[(rsum, i)]