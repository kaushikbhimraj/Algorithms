"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list. 

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

class Node:
	def __init__(self, val):
		self.val = val
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = Node(None)

	def insert(self, value):
		node = self.head
		if not node.val:
			node.val = value
		else:
			while node.next:
				node = node.next
			node.next = Node(value)

	def show(self):
		node = self.head
		while node:
			print(node.val)
			node = node.next

"""
When adding linked lists, 
	- make sure to handle the length of the linked lists 
	- handle the carry after adding each node from each list
	- if there is still a carry left add it to the linked list in the end. 
"""
class Add_Linked_Lists:
	def addTwoNumbers(self, l1, l2):
		node1, node2 = l1, l2
		carry = 0

		node3 = LinkedList()

		while node1 and node2:
			tot = node1.val + node2.val + carry
			carry, tot = self.add_helper(tot)
			node1 = node1.next
			node2 = node2.next
			node3.insert(tot)

		while node1:
			tot = node1.val + carry
			carry, tot = self.add_helper(tot)
			node1 = node1.next
			node3.insert(tot)

		while node2:
			tot = node2.val + carry
			carry, tot = self.add_helper(tot)
			node2 = node2.next
			node3.insert(tot)

		if carry:
			node3.insert(carry)

		return node3.show()

	def add_helper(self, tot):
		if tot > 9:
			return [tot//10, tot%10]
		return [0, tot]


# Driver Code

# First Linked List
arr_1 = [9,3,4,1,1]
a = LinkedList()
for val in arr_1:
	a.insert(val)
a.show()
print("\n")

# Second Linked List
arr_2 = [8,3,2,5]
b = LinkedList()
for val in arr_2:
	b.insert(val)
b.show()
print("\n")

# Addition of two of the linked lists
Add_Linked_Lists().addTwoNumbers(a.head, b.head)