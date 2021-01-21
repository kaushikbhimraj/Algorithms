"""
LC. 821: Shortest Distances to a Character

Store all positions of the given character in an array. 
Create a new array to store all distances
Traverse through string and if current position == character position in array
    - remove top position in array. 
    - store it in variable 'prev'
Update distance in distances array and it will be min (curr position - prev, curr position - pos array top)

Note: Make sure pos array exists after all the popping from it. 
      So create a new variable to store the difference from (curr position - pos array top)
      And use it while taking the minimum. 
"""
# T: O(n) ; s: O(n) where n is length of given string. 
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        pos = []
        for i in range(len(S)):
            if ( S[i] == C ):
                pos.append(i)
        
        res = [0] * len(S)
        prev = 10001
        for i in range(len(res)):
            
            if ( pos and i == pos[0] ):
                prev = pos.pop(0)
            
            diff = abs(i - pos[0]) if ( pos ) else 10001
            res[i] = min(abs(i - prev), diff)
        
        return res