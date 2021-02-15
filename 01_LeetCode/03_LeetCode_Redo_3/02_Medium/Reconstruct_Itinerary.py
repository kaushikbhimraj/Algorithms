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

    # Create an adjacency matrix
    # Values for each key in adj matix hash map will be a heap. 
    # Use depth first search through adj matrix. 
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        routes = defaultdict(list)
        for ticket in tickets:
            heappush(routes[ticket[0]], ticket[1])

        stack = []
        self.dfs(stack, routes, 'JFK')
        
        # Since the return on the DFS will be a stack (all values are reverse order)
        res = []
        i = len(stack) - 1
        while (i >= 0):
            res.append(stack[i])
            i -= 1

        # Return populated output. 
        return res
    
    # Load the heap for the key(start). 
    # Check if heap exists and then proceed to pop the top from heap and use it as start for 
    # the next recursion. Once the while loop is done, add the start value to output array.
    def dfs(self, stack, routes, start):
        heap = routes[start]
        while heap:
            end = heappop(heap)
            self.dfs(stack, routes, end)
        stack.append(start)