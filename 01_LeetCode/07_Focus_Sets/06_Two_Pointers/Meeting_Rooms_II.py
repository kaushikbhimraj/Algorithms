"""
Given an array of meeting time intervals `intervals` where `intervals[i] = [starti, endi]`, return *the 
minimum number of conference rooms required*.

**Example 1:**
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

**Example 2:**
Input: intervals = [[7,10],[2,4]]
Output: 1

"""

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        heappush(heap, intervals[0][1])
        
        for i in range(1, len(intervals)):
            # if end time on heap is less than or equal to the start time
            # of another meeting, pop the top and push the current end time. 
            if (heap[0] <= intervals[i][0]):
                heappop(heap)
            
            heappush(heap, intervals[i][1])
        
        return len(heap)