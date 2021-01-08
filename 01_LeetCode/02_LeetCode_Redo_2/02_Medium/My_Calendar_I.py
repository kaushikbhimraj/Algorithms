# Create a tree and insert the start and end times into the tree. 
# If either the start or the end periods don't fit in then through a False. 

# Creating a Tree Object. 
# This object will have the start and end values.
class Tree:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None
    
    # This function inserts values into the Tree. duh!
    # But will take a tree node as a parameter. 
    def insert(self, node):
        
        # either node.end is less than or equal to tree.start or 
        # node.start is greater than or equal to tree.end, traverse the tree. 
        if node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        
        elif node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        else:
            return False
        

class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Tree(start, end)
            return True
        return self.root.insert(Tree(start, end))


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)