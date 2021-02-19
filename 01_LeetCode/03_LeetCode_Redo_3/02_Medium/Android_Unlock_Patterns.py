"""
Android devices have a special lock screen with a 3 x 3 grid of dots. Users can set an "unlock pattern" 
by connecting the dots in a specific sequence, forming a series of joined line segments where each 
segment's endpoints are two consecutive dots in the sequence. A sequence of k dots is a valid unlock 
pattern if both of the following are true:

All the dots in the sequence are distinct.
If the line segment connecting two consecutive dots in the sequence passes through any other dot, the 
other dot must have previously appeared in the sequence. No jumps through non-selected dots are allowed.
Here are some example valid and invalid unlock patterns:


The 1st pattern [4,1,3,6] is invalid because the line connecting dots 1 and 3 pass through dot 2, but 
dot 2 did not previously appear in the sequence.

The 2nd pattern [4,1,9,2] is invalid because the line connecting dots 1 and 9 pass through dot 5, but 
dot 5 did not previously appear in the sequence.

The 3rd pattern [2,4,1,3,6] is valid because it follows the conditions. The line connecting dots 1 and 3 
meets the condition because dot 2 previously appeared in the sequence.

The 4th pattern [6,5,4,1,9,2] is valid because it follows the conditions. The line connecting dots 1 and 
9 meets the condition because dot 5 previously appeared in the sequence.

Given two integers m and n, return the number of unique and valid unlock patterns of the Android grid 
lock screen that consist of at least m keys and at most n keys.

Two unlock patterns are considered unique if there is a dot in one sequence that is not in the other, 
or the order of the dots is different.
"""

class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        
        # Back tracking. 
        # Stopping condition: when you reach zero on limit. 
        # For each value, check pair (curr_val, next_val) for next_val from [1, 9]
        # Check if next_val is not seen, pair is not in middle or middle[pair] is in seen. 
        # If this condition is true, add the next to the set and continue recursion. 
        # Once you returning on the recursion stack, make sure to remove the values in the set. 
        # Then simply return the count, in this case ans
        def backtrack(curr_val, end):
            if (end == 0):
                return 1
            ans = 0
            for next_val in range(1, 10):
                if (next_val not in seen and ((curr_val, next_val) not in middle or middle[(curr_val, next_val)] in seen)):
                    seen.add(next_val)
                    ans += backtrack(next_val, end-1)
                    seen.remove(next_val)
            return ans

        # Map to check if we are skipping the middle value on dial.
        middle = {
            (1,3):2,
            (3,1):2,
            (1,7):4,
            (7,1):4,
            (3,9):6,
            (9,3):6,
            (7,9):8,
            (9,7):8,
            (1,9):5,
            (9,1):5,
            (3,7):5,
            (7,3):5,
            (2,8):5,
            (8,2):5,
            (4,6):5,
            (6,4):5
        }
        
        ans = 0
        # Looping through all values between m and n.
        # For each value b/w m and n, pair it with every value from 1 to 9 
        for i in range(m, n + 1):
            for j in range(1, 10):
                seen = set([j])
                ans += backtrack(j, i-1)
        return ans