"""
Write a function that takes in a string and returns its longest substring without duplicate characters. 
You can assume that there will only be one longest substring without duplication.

INPUT:
string = "clementisacap"

OUTPUT:
mentisac
"""

def longestSubstringWithoutDuplication(string):
	# Need a cache to store all the visited characters
	# Need a (start, end) coordinate to record the max length
	trackPrevious = {}
	location = [0,1]
	startIdx = 0
	
	for index, char in enumerate(string):
		
		if char in trackPrevious:
			startIdx = max(startIdx, trackPrevious[char] + 1)
		
		if location[1]-location[0] < index+1 - startIdx:
			location = [startIdx, index+1]
		
		trackPrevious[char] = index
	return string[location[0]:location[1]]