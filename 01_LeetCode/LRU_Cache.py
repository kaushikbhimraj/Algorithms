"""
Design and implement a data structure for Least Recently Used (LRU) cache. 
It should support the following operations: get and put. 

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, 
otherwise return -1

put(key, value) - Set or insert the value if the key is not already present. When the cache 
reached its capacity, it should invalidate the least recently used item before inserting a 
new item. 

The cache is initialized with a positive capacity. 

Follow up:
Could you do both operations in O(1) time complexity?

Example:
	LRUCache cache = new LRUCache( 2 /* capacity */ );

	cache.put(1, 1);
	cache.put(2, 2);
	cache.get(1);       // returns 1
	cache.put(3, 3);    // evicts key 2
	cache.get(2);       // returns -1 (not found)
	cache.put(4, 4);    // evicts key 1
	cache.get(1);       // returns -1 (not found)
	cache.get(3);       // returns 3
	cache.get(4);       // returns 4


Note:
	This problem is very keen on data structures and catch how the system could fail. (Really awesome question)
	Main questions to ask 
		
		THINGS TO WATCH OUT FOR
		keys are same and cache limit > 2 (still not fixed)
		keys may not be equal to values
		cache limit = 1

["LRUCache","put","put","get","put","get","put","get","get","get"]
[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
["LRUCache","put","put","get","put","put","get"]
[[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]
["LRUCache","put","get","put","get","get"]
[[1],[2,1],[2],[3,2],[2],[3]]
["LRUCache","put","get"]
[[1],[2,1],[2]]
["LRUCache","put","put","get","put","get","get"]
[[2],[2,1],[1,1],[2],[4,1],[1],[2]]

"""

class LRUNode:


	def __init__(self, val):
		self.val  = val
		self.key  = None
		self.prev = None
		self.next = None
 

class LRUCache:


	def __init__(self, capacity: int):
		# Setting the head and tail to same node. 
		self.limit = capacity
		self.head  = self.tail = LRUNode(None)
		self.count = 1
		self.cache = {}


	def get(self, key: int) -> int:
		# Check if node is tail, move node to head and return value. 
		if self.checkCache(key):
			node = self.cache[key]

			if self.head.val == self.tail.val:
				return self.head.val

			if not node.next:
				self.tail 	= node.prev

			node.prev.next  = node.next
			node.prev       = None
			self.move2Head(node)

			return self.head.val
		else:
			return -1


	def put(self, key: int, value: int) -> None:
		# Check whether key and update node value if present, else you create new node and make it head.
		# Check if the LL is None (head == tail)
		# Check if exceed limit and remove tail if so. 
		if self.checkCache(key):
			node            = self.cache[key]
			node.val        = value
			self.move2Head(node)
		else:
			putNode         = LRUNode(value)
			putNode.key     = key
			self.cache[key] = putNode

			if self.head.val == self.tail.val == None:
				self.head = self.tail = putNode
			else:
				self.move2Head(putNode)
				self.count += 1

				if self.count > self.limit:
					self.remove(self.tail.key)
					self.count -= 1


	def move2Head(self, node):
		# Put node ahead of head and make it the new head. 
		node.next       = self.head
		self.head.prev  = node
		self.head       = node


	def remove(self, key):
		# Retrieve from dictionary, delete in LL and then delete from dictionary. 
		node           = self.cache[key]
		self.tail      = node.prev
		node.prev.next = node.next
		node.next 	   = None
		node.prev 	   = None
		node.val  	   = None
		del self.cache[key]


	def checkCache(self, key):
		# Check if node exists in dictionary.
		try:
			self.cache[key]
			return True
		except KeyError:
			return False


	def show(self):
		# Print all node.val in dictionary.
		print("\n")
		for key in self.cache.keys():
			node = self.cache[key]
			print(key, ": ", node.val, node.prev.val, node.next.val)
		print("\n")


"""
# Test Case #1
x = LRUCache(1)
x.put(2,1)
print(x.get(2))
print("\n")

# Test Case #2
x = LRUCache(2)
x.put(1,1)
x.put(2,2)
print(x.get(1))
x.put(3,3)
print(x.get(2))
x.put(4,4)
print(x.get(1))
print(x.get(3))
print(x.get(4))
print("\n")

# Test Case #3
x = LRUCache(1)
x.put(2,1)
print(x.get(2))
x.put(3,2)
print(x.get(2))
print(x.get(3))
print("\n")

# Test Case #4
x = LRUCache(1)
x.put(2,1)
x.put(2,2)
print(x.get(2))
x.put(1,1)
x.put(4,1)
print(x.get(2))
print("\n")
"""

# Test Case #5
# Failing this test 
x = LRUCache(2)
x.put(2,1)
x.put(1,1)
print(x.get(2))
x.put(4,1)
print(x.get(1))
print(x.get(2))
print("\n")