"""
Given a list of scores of different students, return the average score of each student's 
top five scores in the order of each student's id.

Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  
The average score is calculated using integer division.

 

Example 1:

Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation: 
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.
 

Note:

1 <= items.length <= 1000
items[i].length == 2
The IDs of the students is between 1 to 1000
The score of the students is between 1 to 100
For each student, there are at least 5 scores
"""

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

    	# Organize scores of each student in to a dicitonary. O(n)
        students = {}
        for i in range(len(items)):
            if items[i][0] in students:
                students[items[i][0]].append(items[i][1])
            else:
                students[items[i][0]] = [items[i][1]]
        
        # Create heap to push all scores of each student and only pop top 5
        # heapq has two hidden functions, _heapify_max, _heappop_max for max heap operations. 
        results = []

        # Loading all scores of each student into a max heap. O(n)
        for student in students:
            scores = students[student]
            heapq._heapify_max(scores)
            
            # Only popping five values from max heap. 
            # Take five averages and append it results. 
            average = 0
            for i in range(5):
                average += heapq._heappop_max(scores)
            results.append([student, average//5])
        
        return results
