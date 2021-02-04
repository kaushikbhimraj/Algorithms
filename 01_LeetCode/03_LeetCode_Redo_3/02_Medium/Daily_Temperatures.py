"""
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you 
how many days you would have to wait until a warmer temperature. If there is no future day for which 
this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should 
be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer 
in the range [30, 100].

"""
# T: O(n); S: O(W): w is the max difference between values and n is len of input array
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0] * len(T)
        
        # Starting from right
        # add every value to stack.
        # remove top of stack if curr val greater
        # then if stack is not empty and top of stack is greater than curr value
        #   populate output array with difference b/w location @ top value - location @ curr value
        # after loop return output array. 
        n = len(T) - 1
        while (n >= 0):

            # If top number is equal to curr number in stack we still dont care for it. 
            while (stack and stack[-1][0] <= T[n]):
                stack.pop()

            # Only numbers greater than current temperatures get to be considered. 
            if (stack and T[n] < stack[-1][0]):
                res[n] = stack[-1][1] - n
            stack.append((T[n], n))
            n -= 1
        
        return res