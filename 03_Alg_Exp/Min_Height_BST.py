"""
Write a function that takes in a non-empty sorted array of distinct integers, constructs 
a BST from the integers, and returns the root of the BST. 

The function should minimize the height of the BST. 

You've been provided with a BST class that you'll have to use to construct the BST. 

Each BST node has an integer value, a left child node, and a right child node. A node is
said to be valid BST node if and only if it satisfies the BST property: its value is 
strictly greater than the value of every node to its left; its value is less than or 
eqwual to the values of every node to its right; and its children nodes are either valie
BST nodes themselves or None/null. 

A BST is valid if and only if all of its nodes are valid BST nodes. 

Note that the BST class already has an insert method which you can use if you want. 

INPUT:
array = [1, 2, 5, 7, 10, 13, 14, 15, 22]

OUTPUT:
Sample Output

			10
		  /    \
		 2  	14
		/ \     / \
	   1   5   13  15
	        \       \
	         7       22



Pick the mid of the array. 
Insert it. 
Pick mid of the left array. 
Insert it. 
Pick the mid of the right array. 
Insert it. 
Pick the mid of the left of left array. 
Insert it. 
So on.....

This can be done using recursion. 
"""

def minHeightBst(array):
	return constructMinHeightBST(array, None, 0, len(array)-1)

def constructMinHeightBST(array, bst, leftIdx, rightIdx):
	if leftIdx > rightIdx:
		return 

	# Find the mid value in the array
	midIdx = (leftIdx+rightIdx)//2
	newBstNode = BST(array[midIdx])
	if bst is None:
		bst = newBstNode
	else:
		if array[midIdx] < bst.value:
			bst.left = newBstNode
			bst = bst.left
		else:
			bst.right = newBstNode
			bst = bst.right
	constructMinHeightBST(array, bst, leftIdx, midIdx-1)
	constructMinHeightBST(array, bst, midIdx+1, rightIdx)
	return bst

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)