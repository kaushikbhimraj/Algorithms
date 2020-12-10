"""
In some array arr, the values were in arithmetic progresion: the values arr[i+1] - arr[i] 
are all equal for every 0 <= i < arr.length - 1.

Then, a value from arr was removed that was not the first or last value in the array. 

Return the removed value. 

Example 1:
Input: arr = [5,7,11,13]
Output: 9
Explanation: The previous array was [5,7,9,11,13].

Example 2:
Input: arr = [15,13,12]
Output: 14
Explanation: The previous array was [15,14,13,12].

Constraints:
3 <= arr.length <= 1000
0 <= arr[i] <= 10^5
"""

class Solution:
	def missingNumber(self, arr: List[int]) -> int:
		left, right = 0, len(arr)-1
		diff = int((arr[-1] - arr[0])/len(arr))

		while left < right:
			mid = int((left + right)/2)
			if arr[mid] == arr[0] + (mid * diff):
				left = mid + 1
			else:
				right = mid

		return a[0] + (left * diff)