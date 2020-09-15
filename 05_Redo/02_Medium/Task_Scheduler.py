"""
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a 
different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of 
time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the 
same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
 

Constraints:

1 <= task.length <= 104
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100].
"""


from collections import Counter

# Given tasks, CPU can perform each task sequencially, 
# based on the cooldown period the CPU will be able to perform a certain task only after the cooldown
# period. So if cd = 2, then after finishing task A, CPU will either be idle or finish other tasks until 
# it can again take up task A. 

# This is an easy but tricky math problem. 

# This can be two cases. 
# Case 1: 
# If the most frequent task can be adjusted in a way the all other tasks can fit into the 
# original length of array. 

# Case 2:
# Otherwise there are m tasks are might have the same number of max frequencies or max frequency
# might not be enough to conver the span of the array. 

# Based on the most frequent task and cooldown time we could create an arrangement. 
# For example, n = 3 and tasks = [A, A, A, B, B, B]
# Arrangement: A _ _ _ A _ _ _ A for all As. 
#              A B _  _  A B _  _  A B
#              A B Id Id A B Id Id A B
#             (        )(        )(   )
# Can be categorized into three sections. 
# A B Id Id = (n + 1)
# This (n + 1) repeats for f_max - 1 times. Where f_max is the task with max frequency. 
# Lastly, third sections is since A and B both have same max frequency, 
# # of tasks with max frequency n_max = 2
# So all together (n + 1)(f_max - 1) + n_max

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Since the tasks are all alphabets, there can only be 26 kinds of tasks. 
        frequencies = [0] * 26
        
        for task in tasks:
            frequencies[ord(task)-ord('A')] += 1
            
        f_max = max(frequencies)
        n_max = frequencies.count(f_max)
        
        return max(len(tasks), (n + 1) * (f_max - 1) + n_max)