"""
LC.253 Meeting Rooms II
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number 
of conference rooms required. 

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1
 
Constraints:
1 <= intervals.length <= 104
0 <= starti < endi <= 106

T: O(n); S: O(n), where n number of intervals.
"""

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if (not intervals):
            return 0
        
        intervals.sort()
        heap = []
        heappush(heap, intervals[0][1])
        
        for i in range(1, len(intervals)):
            if ( intervals[i][0] >= heap[0] ):
                heappop(heap)
            heappush(heap, intervals[i][1])
        
        return len(heap)