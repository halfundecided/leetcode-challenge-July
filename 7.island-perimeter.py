"""
July 7, 2020
Island Perimeter
"""


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if grid == None or len(grid) == 0:
            return 0

        perimeter = 0

        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 0:
                    continue
                perimeter += 4
                if i > 0:
                    perimeter -= grid[i-1][j]  # above
                if j > 0:
                    perimeter -= grid[i][j-1]  # left
                if i < len(grid)-1:
                    perimeter -= grid[i+1][j]  # bottom
                if j < len(grid[0])-1:
                    perimeter -= grid[i][j+1]

        return perimeter
