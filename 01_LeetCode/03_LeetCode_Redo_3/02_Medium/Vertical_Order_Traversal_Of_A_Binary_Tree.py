"""
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (x, y), its left and right children will be at positions (x - 1, y - 1) 
and (x + 1, y - 1) respectively.

The vertical order traversal of a binary tree is a list of non-empty reports for each unique 
x-coordinate from left to right. Each report is a list of all nodes at a given x-coordinate. The 
report should be primarily sorted by y-coordinate from highest y-coordinate to lowest. If any two 
nodes have the same y-coordinate in the report, the node with the smaller value should appear earlier.

Return the vertical order traversal of the binary tree.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: Without loss of generality, we can assume the root node is at position (0, 0):
The node with value 9 occurs at position (-1, -1).
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2).
The node with value 20 occurs at position (1, -1).
The node with value 7 occurs at position (2, -2).

Example 2:
Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation: The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report [1,5,6], the node with value 5 comes first since 5 is smaller than 6.
 
Constraints:
The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 1000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# T: O(N log N); S: O(N) where N is number of nodes in binary tree.

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        numList = []
        self.helper(root, 0, 0, numList)
        
        # Based on column -> row -> value priority sort numList. 
        print(numList)
        numList.sort()
        print(numList)
        
        # Create two arrays.
        # First array is to load all values for each column. 
        # In second array, first array is appended and each time the column changes. 
        curr_col = numList[0][0]
        out = []
        temp = []
        for col, row, val in numList:
            if (col == curr_col):
                temp.append(val)
            else:
                out.append(temp)
                temp = [val]
                curr_col = col
                
        # Note: After the process, make sure to add temp once more!
        out.append(temp)
        
        return out
    
    # Helper function for DFS & numList.
    def helper(self, root, col, row, numList) -> None:
        if (not root):
            return
        
        numList.append((col, row, root.val))
        
        self.helper(root.left, col - 1, row + 1, numList)
        self.helper(root.right, col + 1, row + 1, numList)
        