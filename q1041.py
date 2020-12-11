import numpy as np


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direction_index = 0
        current = np.array([0, 0])
        for i in instructions:
            if i == "G":
                current = np.add(current, direction[direction_index])
            elif i == "L":
                direction_index = (direction_index + 1) % 4
            else:
                direction_index = (direction_index - 1) % 4
        if direction_index != 0:
            return True
        return current[0] == 0 and current[1] == 0
