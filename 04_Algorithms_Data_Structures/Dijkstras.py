"""
Algorithm steps:

    - Find cheapest node
    - Update code of the neighbors of this node
    - Repeat unitl youve done this for every node in graph
    - Calculate the final path

Runtime
    - Space complexity: 
    - Time complexity:  

Just like breadth first in Dijkstra's you will look at all the neighboring nodes but look only at the weights.
"""

class Node:
    def __init__(self, value):
        self.vall = value
        self.cost = float("inf")
        self.neighbors = []

F = ['Kaushik', 'Abhishek', 'New Jersey', 'Flinestone']
A = ['A', 'B', 'C', 'D', 'E']

for i in F:
    a = Node(i).neighbors
    


# Costs:    
# Graphs:  
# Parents: 

