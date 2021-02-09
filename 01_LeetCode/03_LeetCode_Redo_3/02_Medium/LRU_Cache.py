# Least Recently Used Cache
# Cache needs to be keep track of the sequence of how the values have been inserted. 
# If GET is used against a value, you'd have to bring the value to the top of the cache. 

# GET => if value is in list, return it and bring it to the start of the list. 
# PUT => if new value is put into list, it needs to be on top of the list. 

class Node:
    def __init__(self):
        self.key = -1
        self.val = -1
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        self.size = 0
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    # Insert new node b/w head node and its next node. 
    # Point newNode.next to head's next node. 
    # Make head.next.prev point back to new node. 
    # Then point head.next to newNode.
    # Finally point newNode.prev to head
    def add_top(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
    
    # Point node's prev to node's next
    # Point node's next.prev to prev
    def pop_node(self, node):
        prevNode = node.prev
        prevNode.next = node.next
        node.next.prev = prevNode
    
    # Avoids repetition
    def move_top(self, node):
        self.pop_node(node)
        self.add_top(node)    
    
    # Remove node before tail and return that node. 
    def remove_tail(self):
        prev = self.tail.prev
        self.pop_node(prev)
        return prev
    
    def get(self, key: int) -> int:
        if (key in self.map):
            self.move_top(self.map[key])
            return self.map[key].val
        
        else:
            return -1
    
    # CASE 1: STEP 1:
    # Check if key exists in dictionary. 
    # If not, create a new node and add it to dictionary. 
    # Only then add node to top and increment size.
    # CASE 1: STEP 2:
    # Check size > capacity
    # If so, remove tail node and then remove from dictionary.
    # CASE 2: STEP 1:
    # If node already exists, simply update the value for that node
    # Move node to top. 
    def put(self, key: int, value: int) -> None:
        node = self.map.get(key, None)
        
        if not node:
            newNode = Node()
            newNode.key = key
            newNode.val = value
            self.map[key] = newNode
            self.add_top(newNode)
            self.size += 1
            
            if (self.size > self.cap):
                node = self.remove_tail()
                del self.map[node.key]
                self.size -= 1
                
        else:
            node.val = value
            self.move_top(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)