

"""
RECURSIVE AND DYNAMIC PROGRAMMING

Question 8.1
Name:    Triple Set
Desc: 	 A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. 
		 Implement a method to count how many possible ways the child can run up the stairs. 

"""

class Steps:
	def __init__(self):
		self.count = 0
		self.cache = {}

	def triple(self, steps):
		self.count += 1

		if steps in self.cache:
			return self.cache[steps]

		if steps < 0:
			return 0

		if steps == 0:
			return 1

		value = self.triple(steps-1) + self.triple(steps-2) + self.triple(steps-3)
		self.cache[steps] = steps
		return self.count


print(Steps().triple(3))