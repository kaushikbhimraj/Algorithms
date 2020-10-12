"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Time: O(n)
Space: O(1)
"""


class Solution:
	def merge(self, intervals):

		# Sort the array first to make sure the intervals are all lined up properly. 
		i = 1
		intervals.sort()

		while i < len(intervals):

			# Values are compared between the current and previos elements of array.
			# Each element contains two values [small, big]

			# Condition 1: Compare current value: small <= previous value: big 
			#                      current value: big   >= previous value: big 
			if intervals[i-1][1] >= intervals[i][0] and intervals[i][1] >= intervals[i-1][1]:
				intervals[i][0] = min(intervals[i-1][0], intervals[i][0])
				intervals.pop(i-1)

			# Condition 2: Compare current value: small > previous value: big 
			#                      current value: big   < previous value: big 
			elif intervals[i-1][1] >= intervals[i][0] and intervals[i][1] < intervals[i-1][1]:
				intervals[i][0] = min(intervals[i-1][0], intervals[i][0])
				intervals[i][1] = max(intervals[i-1][1], intervals[i][1])
				intervals.pop(i-1)

			else:
				i += 1

		return intervals


# Test cases
a = [[1,3],[2,6],[8,10],[15,18]]
b = [[1,4],[4,5]]
c = [[1,4],[0,4]]
d = [[1,4],[0,1]]
e = [[3,6],[2,6],[1,6]]
f = [[1,4],[2,3]]
g = [[1,4],[0,0]]

x = Solution()
x.merge(a)

print(x.merge(a))
print(x.merge(b))
print(x.merge(c))
print(x.merge(d))
print(x.merge(e))
print(x.merge(f))
print(x.merge(g))