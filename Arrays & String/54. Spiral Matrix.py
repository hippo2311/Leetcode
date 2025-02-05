from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3  
        output = []
        direction = RIGHT
        i, j = 0, 0  

        UP_WALL = 0
        RIGHT_WALL = len(matrix[0]) - 1
        LEFT_WALL = 0
        DOWN_WALL = len(matrix) - 1

        while len(output) < len(matrix) * len(matrix[0]): 
            if direction == RIGHT:
                while j <= RIGHT_WALL:  
                    output.append(matrix[i][j])
                    j += 1
                j -= 1  # Step back
                i += 1  # Move down
                UP_WALL += 1  
                direction = DOWN

            elif direction == DOWN:
                while i <= DOWN_WALL: 
                    output.append(matrix[i][j])
                    i += 1
                i -= 1  # Step back
                j -= 1  # Move left
                RIGHT_WALL -= 1  
                direction = LEFT

            elif direction == LEFT:
                while j >= LEFT_WALL:  # Move left
                    output.append(matrix[i][j])
                    j -= 1
                j += 1  # Step back
                i -= 1  # Move up
                DOWN_WALL -= 1  
                direction = UP

            elif direction == UP:
                while i >= UP_WALL:  # Move up
                    output.append(matrix[i][j])
                    i -= 1
                i += 1  # Step back
                j += 1  # Move right
                LEFT_WALL += 1  
                direction = RIGHT

        return output 
# Time: O(n)
# Space: O(1)
