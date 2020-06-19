"""
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

Constraints:

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.


Notes:
	PROCESS
	For the letter logs, separate log from identifier
	Push both the separated and complete log in a tuple to heap. 
	Pop the heap to get sort 
	Merge sorted array with the original logs array. 
"""

from heapq import heappush, heappop

class Solution:
	def reorderLogFiles(self, logs: List[str]) -> List[str]:
		newHeap = []
		sorted_logs = []
		i = 0

		# Separate letter logs from digit logs. 
		while i < len(logs):
			# Split the string from its idetifier. 
			tail = logs[i].split(" ",1)[1]
			if not tail[0].isdigit():
				log = logs.pop(i)
				heappush(newHeap, (tail, log))
			else:
				i += 1

		while newHeap:
			sorted_logs.append(heappop(newHeap)[1])
		return sorted_logs + logs


a = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
x = Solution()
print(x.reorderLogFiles(a))

