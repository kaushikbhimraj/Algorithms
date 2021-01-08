"""
Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you 
find more than one maximum elements, only remove the top-most one.


Example 1:
MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
Note:
-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.
"""

# Time:  O(n) for popMax
# Space: O(n) 

class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxStack = []
        self.stack = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.maxStack or x >= self.maxStack[-1]:
            self.maxStack.append(x)
    
    # When popping value from mainstack, check to see if top value on maxStack 
    # is also the same value. 
    def pop(self) -> int:
        if self.maxStack[-1] == self.stack[-1]:
            self.maxStack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        if self.maxStack:
            return self.maxStack[-1]
    
    # Here you popping the max value from stack and return it. 
    # 1. val = Pop value from maxStack 
    # 2. Iterate through values in mainStack and pop values from right until you reach 'val'
    # 3. Store the values that are being removed in another array. 
    # 4. Pop the final value after you found it (do not add it the new array)
    # 5. Push all values from the new array back using self.push(). 
    # return val. :)
    def popMax(self) -> int:
        val = self.maxStack.pop()
        b = []
        while self.stack[-1] != val:
            b = [self.stack.pop()] + b
            
        self.stack.pop()
        for i in range(len(b)):
            self.push(b[i])
        
        return val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()