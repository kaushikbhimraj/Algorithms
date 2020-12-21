"""
You are given an immutable linked list, print out all values of each node in reverse with the 
help of the following interface:
	ImmutableListNode: An interface of immutable linked list, you are given the head of the 
	list. 

You need to use the following function to access the linked list (you can't access the 
ImmutableListNode directly):
	ImmutableListNode.printValue(): Print value of the current node. 
	ImmutableLIstNode.getNext(): Return the next node. 

The imput is only given to initialize the linked list internally. You must solve this problem
without modifying the linked list. In other words, you must operate the linked list using only 
the mentioned APIs. 
"""

# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

# Use recursion stack to print value in reverse order. 
class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        self.dfs(head)
    
    def dfs(self, head):
        if not head:
            return
        
        self.dfs(head.getNext())
        head.printValue()