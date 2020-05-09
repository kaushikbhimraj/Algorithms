"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Input: J = "aA", S = "aAAbbbb"
"""

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # First thing that pop into mind is to use a hash table and store all the values of J in it. 
        # Then iterating through S we can identify the values that exist in J and count up. 
        bag_of_precious_stones = {}
        for stone in J:
            bag_of_precious_stones[stone] = stone
        
        # Counting only the stones types from J in S. 
        count_my_gems = 0
        for stone in S:
            try:
                bag_of_precious_stones[stone]
                count_my_gems += 1
            except KeyError:
                pass
        return count_my_gems