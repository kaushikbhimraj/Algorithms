"""
Title: Defanging an IP address
Given a valid (IPv4) IP address, return a defanged version of that IP address. 

A defanged IP address replaces every period "." with "[.]"

Example:

Input: 	"1.1.1.1"
Output: "1[.]1[.]1[.]1"

Questions:
	Is the Ip address of fixed length?
	IPv4: 32 
"""

class Solution:

	# OTB functionality in Python (easy route out)
	def easy(self, address):
		return address.replace(".", "[.]")

	# Need to use a helper function to process the index jumps. 
	# Bits after the last periods are appended in the last step. 
	def defangIPaddr(self, address: str) -> str:
		if not address:
			return None
		index = 0
		new_string = ""
		while index < len(address) - 1:
			val = self._helper_function(index, address)
			print(val)
			index = val[0]
			new_string += val[1]
		return new_string + address[index:]

	def _helper_function(self, index, address):
		if index + 1 < len(address) and address[index + 1] == ".":
			print(address[index:index+1] + "[.]")
			return index + 2, address[index:index+1] + "[.]"
			
		if index + 2 < len(address) and address[index + 2] == ".":
			print(address[index:index+2] + "[.]")
			return index + 3, address[index:index+2] + "[.]"
		
		if index + 3 < len(address) and address[index + 3] == ".":
			print()
			return [index + 4, address[index:index+3] + "[.]"]
	

y = "227.222.40.237"
x = "1.1.1.1"
S = Solution()
print("Input:", y)
print("OTB defang output:                   ", S.easy(y))
print("This using the defang IPaddr method: ", S.defangIPaddr(y))
