"""
Write a BST class for a Binary Search Tree. The class should support:
    - Inserting values with the insert method. 
    - Removing values with the remove method; this method should only remove the first instance of a given value.
    - Searching for values with the contains method. 

Note that you can't remove values from a single-node tree. In other words, calling the remove method on a single-node
tree should simply not do anything. 

Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST node
if and only if satisfies  the BST property: its value is strictly greater than the values of every node to its left; 
its value is less than or equal to the values of every node to its right; and its children nodes are either valid 
BST nodes themselves or None/null. 

"""

# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.


class BST:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.

        if self.value > value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

        return self

    def contains(self, value):
        # Write your code here.

        if self.value > value:
            if self.left is None:
                return False
            return self.left.contains(value)

        elif self.value < value:
            if self.right is None:
                return False
            return self.right.contains(value)

        else:
            return True

    def remove(self, value, parent=None):
        # Write your code here.
        # Do not edit the return statement of this method.
        if self.value > value:
            if self.left is not None:
                self.left.remove(value, self)
        elif value > self.value:
            if self.right is not None:
                self.right.remove(value, self)

        else:
            if self.left is not None and self.right is not None:
                self.value = self.right.getMinValue()
                self.right.remove(self.value, self)

            elif parent is None:
                if self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left  = self.left.left
                elif self.right is not None:
                    self.value = self.right.value
                    self.left  = self.right.left
                    self.right = self.right.right
                else:
                    pass
            elif parent.left == self:
                parent.left = self.left if self.left is not None else self.right
            elif parent.right == self:
                parent.right = self.left if self.left is not None else self.right

        return self

    def getMinValue(self):
        if not self.left:
            return self.value
        return self.left.getMinValue()
