"""
Given n non-negative integers a1, a2, ..., an , where each represents a point 
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints 
of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis 
forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""

# Time: O(n)
# Space: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Create two pointers at both ends. 
        # Look from bound with maximum area. 
        maxArea = float("-inf")
        left = 0
        right = len(height) - 1
        
        while left < right:
            
            # Compute area and update maxArea
            # Height -> min of left height and right height
            # Base -> distance between i and j
            currHeight = min(height[left], height[right])
            maxArea = max(maxArea, (right - left)*currHeight)
            
            # Decrement when one columns height is less than the other. 
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return maxArea