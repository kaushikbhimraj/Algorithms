"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
def largestRange(array):

    # Need a value to keep track of the size of the array. 
    # Need a 2 value to store the min and max of the continous range
    longest_length = 0
    longest_length_array = []

    # Need a cache to store all the values from the given array. 
    # The values from the array are the keys and dictionary will have a boolena for the value.
    # This will avoid repetitions in counting. 
    cache = {}
    for val in array:
        cache[val] = True

    # For every value in the main array, check and see if there exists a value -1 and +1 in the dictionary. 
    # And count the number of values and record the count. (while you are doing this also make sure to mark the value you visit
    # in the dictionary as False.)

    for val in array:
        if not cache[val]:
            continue

        cache[val] = False
        current_length = 1

        left = val - 1
        right = val + 1
        
        # Loop to check if the value left of the main value exist in dictionary.
        while left in cache:
            cache[left] = False
            left -= 1
            current_length += 1

        # Loop to check if the value right of the main value exist in dictionary. 
        while right in cache:
            cache[right] = False
            right += 1
            current_length += 1

        # Check and update every iteration if the range is greater than the longest range. 
        # Also the update the 2-value array if the condition is true. 
        if current_length > longest_length:
            longest_length = current_length
            longest_length_array = [left+1, right-1]

    return longest_length_array