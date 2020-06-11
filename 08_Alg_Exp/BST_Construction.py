"""
Write a BST class for a Binary Search Tree. The class should support:
	- Inserting values with the insert method. 
	- Removing values with the remove method; this method should only remove the first instance of a given value. 
	- Searching for values with the contains methods. 

Note that you can't remove values from a single-node tree. In other words, calling the remove method on a single
node tree should simply not do anything. 

Each BST node has an integer value, a left child node and a right child node. A node is said to be a valid BST 
node if and only if it satisfies the BST properly: its value is strictly greater than the values of every node to 
its left; its value is less than or equal to the values of every node to its right; and its children nodes are 
either valid BST nodes themselves or None/null. 

"""

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        return self

    def contains(self, value):
        # Write your code here.
        pass

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        return self
