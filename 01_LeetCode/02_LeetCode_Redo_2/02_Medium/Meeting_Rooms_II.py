"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] 
(si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
"""

from heapq import heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        1. sort intervals w.r.t => sort(key = lambda x: x[0])
        2. push end time of first interval to a heap. 
        3. Iterate through intervals, 
            a. check if end_time <= heap[0]: remove from heap.
            b. push current end time to heap. 
        4. Return len(heap)
        """
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[0])
        free_rooms = []
        
        # Push the first element to heap.
        heappush(free_rooms, intervals[0][1])
        for i in range(1, len(intervals)):
            
            # if start time of current interval > end time of minimum heap
            if free_rooms[0] <= intervals[i][0]:
                heappop(free_rooms)
            
            heappush(free_rooms, intervals[i][1])
        
        return len(free_rooms)