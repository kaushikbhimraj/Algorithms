
"""
Simple trie node contains a dictionary of its neighbouring trie nodes. 
"""
class Node:
    def __init__(self):
        self.next = {}
        self.isEnd = False

class Trie:
	def __init__(self):
		self.root = Node()

	def insert(self, word):
		node = self.root

		for char in word:
			if char not in node.next or not node.next:
				node.next[char] = Node()
			node = node.next[char]

		node.next[''] = Node()
		node.next[''].isEnd = True

	def prefixLookup(self, prefix):
		node = self.root

		# Iterate through the prefix in trie. 
		for char in prefix:
			if char not in node.next:
				return 

			node = node.next[char]

		# Prefix fetch - helper function
		words = []
		self.prefixLookupHelper(node, words, [])

		return [prefix + word for word in words]

	# Helper function to fetch for all similar words. 
	def prefixLookupHelper(self, node, output, combo):
		if (node.isEnd):
			output.append(''.join(combo))
			return

		for key in node.next:
			combo.append(key)
			self.prefixLookupHelper(node.next[key], output, combo)
			combo.pop()


# Unit test cases
x = Trie()
x.insert("sand")
x.insert("saw")
x.insert("string")

print(x.prefixLookup("s"))
