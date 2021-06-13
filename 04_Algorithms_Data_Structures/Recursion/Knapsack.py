
"""
Exploring the knapsack problem first using the recursion and using the dynamic programming. 

Problem:
	Given weights and their prices, only certain amount weight can be carried in a bag. 
	Need to fill the bag with the weights that would the max total price. 
"""

# Decrement the bag capacity when a weight is added to it. 
# In this recursion, you are either adding or no adding to the bag
# You are not adding to the bag when the weight of the object is greater than the weight capacity of the bag.
class knapsack_recursion:
	def bag(self, prices, weights, max_weight):
		return self.bag_helper(prices, weights, max_weight, len(weights)-1)

	def bag_helper(self, prices, weights, totalWeight, idx):
		if (totalWeight == 0 or idx == 0):
			return 0
		
		if (weights[idx] > totalWeight):
			return self.bag_helper(prices, weights, totalWeight, idx-1)

		# Recurrence condition: max of(current_price + recursion(bag_capacity - current_weight), recursion(bag_capacity))
		return max(prices[idx] + self.bag_helper(prices,weights, totalWeight - weights[idx], idx-1), self.bag_helper(prices, weights, totalWeight, idx-1))


# Memoizing the recursion is a simply remmebering the max in a dictionary.
class knapsack_memoization:
	def bag(self, prices, weights, max_weight):
		return self.bag_helper(prices, weights, max_weight, len(weights)-1, {})

	def bag_helper(self, prices, weights, totalWeight, idx, book):
		if (totalWeight == 0 or idx == 0):
			return 0

		if (weights[idx] > totalWeight):
			return self.bag_helper(prices, weights, totalWeight, idx-1, book)

		if (totalWeight in book):
			return book[totalWeight]

		book[totalWeight] = max(prices[idx] + self.bag_helper(prices, weights, totalWeight-weights[idx], idx-1, book), self.bag_helper(prices, weights, totalWeight, idx-1, book))
		return book[totalWeight]