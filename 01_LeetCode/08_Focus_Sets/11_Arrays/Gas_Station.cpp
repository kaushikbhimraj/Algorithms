/*
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station 
to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around 
the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

Example 1:
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:
Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
 
Constraints:
gas.length == n
cost.length == n
1 <= n <= 104
0 <= gas[i], cost[i] <= 104
*/

class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int total_sum = 0;
        int curr_sum = 0;
        int start = 0;

        // Go through all gas stations. 
        // Update start point where the amount of gas at gas station is greater
        // than the cost to get the gas. 
        // Also keep adding all sum to make sure the total gas is >= cost. (In other words
        // it needs to be zero or positive, then you are bound to repeat the circle.)
        
        for (int i=0; i < gas.size(); i++){
            curr_sum += gas[i] - cost[i];
            if (curr_sum < 0){
                curr_sum = 0;
                start = i + 1;
            }
            total_sum += gas[i] - cost[i];
        }
        return (total_sum >= 0) ? start:-1;
    }
};