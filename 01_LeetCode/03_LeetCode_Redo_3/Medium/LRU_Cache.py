# Least Recently Used Cache
# Cache needs to be keep track of the sequence of how the values have been inserted. 
# If GET is used against a value, you'd have to bring the value to the top of the cache. 

# GET => if value is in list, return it and bring it to the start of the list. 
# PUT => if new value is put into list, it needs to be on top of the list. 


class Linked:
    def __init__(self):
        self.key = 0 
        self.value = 0
        self.prev = None
        self.next = None

class LRUCache:
    # current node - previous value should be set to head.
    #              - next value should be set to head.next. 
    # head node    - next value should be set to current node. 
    #              - head.next.previous value should be set to current node. 
    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    # Would have to make the connetion between current node's previous value and
    # its next value. 
    def _remove_node(self, node):
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev

    # This function is used to move which node is used to the top the list. 
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)
    
    # Why?
    def _pop_tail(self):
        res = self.tail.prev
        self._remove_node(res)
        return res

    def __init__(self, capacity):
        self.head, self.tail = Linked(), Linked()
        self.size = 0
        self.capacity = capacity
        self.cache = {}

        self.head.next = self.tail
        self.tail.prev = self.head

    # Simply fetch the value from dictionary, move to top of linkedlist and return value in node.
    def get(self, key):
        if key not in self.cache:
            return -1
        self._move_to_head(key)
        return self.cache[key].value
    
    # Create a new node and add it to list and dictionary. 
    def put(self, key, value):
        node = self.cache.get(key, None)
        if not node:
            newNode = Linked()
            newNode.key = key
            newNode.value = value

            # Build the prev and next values by adding it to the linked list. 
            # Then add it the dictionary.
            self._add_node(newNode)
            self.cache[newNode]
            self.size += 1

            # Check and maintain the cache within the limit. 
            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = value
            self._move_to_head(node)