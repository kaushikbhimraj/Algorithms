"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], 
reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, 
the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical 
order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical 
order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.
Example 1:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
"""
from heapq import heappush, heappop
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Build an adjacency map
        itin = {}
        for x,y in tickets:
            if x in itin:
                heappush(itin[x], y)
            else:
                itin[x] = [y]
        
        res = []
        self.helper("JFK", itin, res)
        return res
    
    def helper(self, start, itin, out):
        if (start not in itin or not itin[start]):
            out.append(start)
            return 
        
        out.append(start)
        newStart = heappop(itin[start])
        return self.helper(newStart, itin, out)
        