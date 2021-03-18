"""
On an infinite plane, a robot initially stands at `(0, 0)` and faces north. The robot can 
receive one of three instructions:

- `"G"`: go straight 1 unit;
- `"L"`: turn 90 degrees to the left;
- `"R"`: turn 90 degrees to the right.

The robot performs the `instructions` given in order, and repeats them forever.

Return `true` if and only if there exists a circle in the plane such that the robot never leaves the circle.
"""


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # 0 - north, 1 - east, 2 - south, 4 - west
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        # Since the staring position of the robot will always be the origin and point to north. 
        current_position = (0,0)
        current_direction = 0
        
        for inst in instructions:
            x = current_position[0]
            y = current_position[1]
            
            if (inst == "G"):
                x = x + directions[current_direction][0]
                y = y + directions[current_direction][1]
                
                current_position = (x,y)
            
            elif (inst == "L"):
                current_direction = (current_direction + 3) % 4
            
            elif (inst == "R"):
                current_direction = (current_direction + 1) % 4
                
        return current_direction != 0 or current_position == (0,0)