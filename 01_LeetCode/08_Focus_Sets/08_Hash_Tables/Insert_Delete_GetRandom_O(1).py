"""
Implement the `RandomizedSet` class:

- `RandomizedSet()` Initializes the `RandomizedSet` object.
- `bool insert(int val)` Inserts an item `val` into the set if not present. Returns `true` if the item was 
not present, `false` otherwise.
- `bool remove(int val)` Removes an item `val` from the set if present. Returns `true` if the item was present, 
`false` otherwise.
- `int getRandom()` Returns a random element from the current set of elements (it's guaranteed that at least one 
element exists when this method is called). Each element must have the **same probability** of being returned.

**Example 1:**

```
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

```

**Constraints:**

- `231 <= val <= 231 - 1`
- At most `105` calls will be made to `insert`, `remove`, and `getRandom`.
- There will be **at least one** element in the data structure when `getRandom` is called.
"""
from random import choice

class RandomizedSet:

    # Store self.map[val] = position in self.pos
    def __init__(self):
        self.map = {}
        self.pos = []
    
    # Check if the value exists in self.map. 
    # If the value exists, don't do anything. 
    # If the value does not exist, add the value to self.map and append self.pos with value. 
    def insert(self, val: int) -> bool:
        if (val in self.map):
            return False
        self.pos.append(val)
        self.map[val] = len(self.pos)-1
        return True
    
    # If the value exists in self.map, get is index and replace is with the last 
    # value from the self.pos and update the self.map with the value from self.pos
    def remove(self, val: int) -> bool:
        if (val in self.map):
            idx = self.map[val]
            temp = self.pos[-1]
            self.pos[idx] = temp
            self.map[temp] = idx
            self.pos.pop()
            del self.map[val]
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.pos)
        
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()