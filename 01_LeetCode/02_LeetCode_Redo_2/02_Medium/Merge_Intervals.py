"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to 
get new method signature.

Constraints:
intervals[i][0] <= intervals[i][1]
"""

# There are mainly two main cases to worry about.
#   - case 1: meeting 1 -> [1, 3]
#             meeting 2 -> [2, 6]
#             3 >= 2 and 3 <= 6
#             logic: [meeting1[0], max(meeting1[1], meeting2[1])]
#             merge -> meeting 2 -> [1, 6]

#   - case 2: meeting 1 -> [1, 3]
#             meeting 2 -> [1, 2]
#             3 >= 1 and 3 > 2
#             logic: [min(meeting1[0], meeting2[0]), max(meeting1[1], meeting2[1])]
#             merge -> meeting 2 -> [1, 3]


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # Edge case 
        if len(intervals) == 1:
            return intervals
        
        # Sort the array w.r.t first element in subarray
        intervals.sort(key=lambda x:x[0])
        i = 1

        # While loop used to catch constant change of lenght in intervals array. 
        while i < len(intervals):
            
            # Previous meeting and current meeting start and end times. 
            a_1 = intervals[i-1][0]
            a_2 = intervals[i-1][1]
            b_1 = intervals[i][0]
            b_2 = intervals[i][1]
        
            # If either of these two cases are true, remove the previous meeting and update the 
            # current meeting end and start times. (Don't increment counter)

            # If the end time of previous meeting is >= start time of current meeting (overlap),
            # check to see if end time of previous is less than end time of current meeting.
            if (a_2 >= b_1 and a_2 <= b_2):
                intervals[i][0] = min(intervals[i-1][0], intervals[i][0])
                intervals.pop(i-1)

            # If the end time of previous meeting is >= start time of current meeting (overlap),
            # check to see if end time of previous is greater than end time of current meeting
            elif (a_2 >= b_1 and a_2 > b_2):
                intervals[i][0] = min(intervals[i-1][0], intervals[i][0])
                intervals[i][1] = max(intervals[i-1][1], intervals[i][1])
                intervals.pop(i-1)

            else:
                i += 1
                
        return intervals