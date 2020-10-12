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
        currentNode = self
        while True:

        	# Check if value is greater/equal or less than the value in current node. 
        	# If you reach a leaf, insert the value in as the child of the node. 

        	# RIGHT
        	if currentNode.value <= value:
        		if not currentNode.right:
        			currentNode.right = BST(value)
        			break
        		else:
        			currentNode = currentNode.right

        	# LEFT
        	else:
        		if not currentNode.left:
        			currentNode.left = BST(value)
        			break
        		else:
        			currentNode = currentNode.left

        # Return the head node. 
        return self


    def contains(self, value):
        # Write your code here.
        currentNode	= self

        # First check value match the node value or else traverse left or right. 
        while currentNode:
        	if currentNode.value == value:
        		return True

        	if currentNode.value < value:
        		currentNode = currentNode.right
        	else:
        		currentNode = currentNode.left
        return False


    def remove(self, value, parentNode=None):
        # Write your code here.
        # Do not edit the return statement of this method.
        currentNode = self

        # Tree main edge cases 
        # 	1. two children are not None
        #	2. node is root node
        # 	3. has one child 

        while currentNode:
    
        	# Traversing BST until reaching node. 
        	# Storing the previous node as its parent node. PRETTY NEAT TRICK!!
        	if currentNode.value < value:
        		parentNode = currentNode
        		currentNode = currentNode.right

        	elif currentNode.value > value:
        		parentNode = currentNode
        		currentNode = currentNode.left
    		
    		# Check above three edge cases after reaching the deletion node. 
        	else:
        		# Case 1:
        		if currentNode.left and currentNode.right:
        			currentNode.value = currentNode.right.getMinValue()
        			currentNode.right.remove(currentNode.value, currentNode)

        		# Case 2:
        		# If the above sequence did not run, then the following code with see if the node is root. 
        		# Also will also check if which of the children is NOT NONE 
        		# And manually the node over the main node.
	        	elif not parentNode:
	        		if currentNode.left:
	        			currentNode.value = currentNode.left.value
	        			currentNode.right = currentNode.left.right
	        			currentNode.left  = currentNode.left.left

	        		elif currentNode.right:
	        			currentNode.value = currentNode.right.value
	        			currentNode.left  = currentNode.right.left
	        			currentNode.right = currentNode.right.right

	        		# If the root node does not have any children, then skip.
	        		else:
	        			pass

        		# Case 3:
        		# This case catches the sequence where there is atleast on 
	        	elif parentNode.left == currentNode:
	        		parentNode.left = currentNode.left if currentNode.left else currentNode.right
	        	elif parentNode.right == currentNode:
	        		parentNode.right = currentNode.left if currentNode.left else currentNode.right
	        	break

        return self

    # Helper function to the left most node in the right sub-tree for a node. 
    def getMinValue(self):
    	currentNode = self
    	while currentNode.left:
    		currentNode = currentNode.left
    	return currentNode.value
