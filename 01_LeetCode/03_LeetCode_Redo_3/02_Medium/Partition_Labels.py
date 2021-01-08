class Solution:
    # Two pointers
    # Find the last position of a character in the stirng. (create dictionary of the last positions)
    # Every iteration, update second pointer with the max value of position. 
    # If position of current iteration equals with max position, we have found SHORTEST substring 
    # that has all characters inclusive and will not be found in the other parts. 
    def partitionLabels(self, S: str) -> List[int]:
        last = {c:i for i, c in enumerate(S)}
        first = second = 0
        res = []
        
        for i,c in enumerate(S):
            second = max(second, last[c])
            
            # MOST IMPORTANT PART!!!
            if i == second:
                res.append(i - first + 1)
                first = i + 1
        
        return res