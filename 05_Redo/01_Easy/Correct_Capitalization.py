"""
This question is asked by Google. Given a string, return whether or not it uses 
capitalization correctly. A string correctly uses capitalization if all letters 
are capitalized, no letters are capitalized, or only the first letter is 
capitalized.

Ex: Given the following strings...

"USA", return true
"Calvin", return true
"compUter", return false
"coding", return true
"""

class Solution:
	def correctCapitalization(self, word):
		# Check for upper case, if not title case. 
		if word.isupper():
			return True
		elif word.istitle():
			return True
		elif word.islower():
			return True
		else:
			return False


a = "USA"
b = "Calvin"
c = "compUter"
d = "coding"

x = Solution()
print(x.correctCapitalization(a))
print(x.correctCapitalization(b))
print(x.correctCapitalization(c))
print(x.correctCapitalization(d))