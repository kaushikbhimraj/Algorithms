"""
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements 
(it's guaranteed that at least one element exists when this method is called). 
Each element must have the same probability of being returned.

Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
"""

from random import choice

# will need 1 dictionary, 1 array. 
# dictionary -> key: value in array, value: location of value in array. 
# array to hold values for O(1) deletion. 

class RandomizeSet:

	def __init__(self):
		self.cache = {}
		self.list = []

	# Ability to insert value in to a database at O(1) time and if value already present, return false. 
	def insert(self, val: int) -> bool:
		if val in self.cache:
			return False

		self.list.append(val)
		self.cache[val] = len(self.list) - 1
		return True

	# Step 1: Get the index of value from the dictionary. 
	# Step 2: Replace value at index with last value in array. 
	# Step 3: Delete last value in array. 
	# Step 4: Update the key with last value with the next index. 
	# Step 5: Delete from dictionary the value that was supposed to deleted. 
	def remove(self, val: int) -> bool:
		if val in self.cache:
			index = self.cache[val]
			self.list[index] = self.list[-1]
			last_element = self.list.pop()
			self.cache[last_element] = index
			del self.cache[val]
			return True
		return False

	# Just need to return value at random index in array. 
	def getRandom(self) -> int:
		return choice(self.list)