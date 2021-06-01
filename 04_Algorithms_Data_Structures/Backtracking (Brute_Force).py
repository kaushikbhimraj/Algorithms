# Reference: https://www.youtube.com/watch?v=DKCbsiDBN6c

# Style - 1: Using a class object to execute backtracking. 
# In this method you will have to declare all the initial values in the parent function, 
# and implement the backtracking in the helper function. 

class Solution():
	def findCombinations(self, students):
		output = []
		if (not students):
			return output

		self.backtracking(students, output, [])
		return output

	def backtracking(self, students, output, combo):
		if (not students):
			output.append(combo[:])
			return 

		for i in range(len(students)):
			combo.append(students[i])
			self.backtracking(students[:i] + students[i+1:], output, combo)
			combo.pop()

# Style - 2
# The recursive function (backtracking) is declared inside the main function, so there is no
# need to pass the initial conditions to the child (nested) function.

def combination(students):
	output = []
	if (not students):
		return output

	def backtracking(inputs, combo):
		if (not inputs):
			output.append(combo[:])
			return

		for i in range(len(inputs)):
			combo.append(inputs[i])
			backtracking(inputs[:i] + inputs[i+1:], combo)
			combo.pop()

	backtracking(students, [])
	return output




# Unit Testing
students = ['B1','B2','G1']

# Style - 1
print("Class Methods")
x = Solution()
print(x.findCombinations(students))

print("\n")

# Stype - 2
print("Nested Functions")
print(combination(students))