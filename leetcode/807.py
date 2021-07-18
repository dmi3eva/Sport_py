from typing import List
from copy import deepcopy

class Solution:
    def rotate90CW(self, grid: List[List[int]]) -> List[List[int]]:
        source_height = len(grid)
        source_width = len(grid[0])
        rotated_grid = [[0 for _ in range(source_height)] for _ in range(source_width)]
        for i in range(source_height):
            for j in range(source_width):
                rotated_grid[j][source_height - 1 - i] = grid[i][j]
        return rotated_grid

    def solve_in_one_direction(self, grid: List[List[int]]) -> List[List[int]]:
        source_height = len(grid)
        source_width = len(grid[0])
        height_grid = [[0 for _ in range(source_height)] for _ in range(source_width)]
        for i in range(source_height):
            visible_value = 0
            for j in range(source_width):
                if grid[i][j] > visible_value:
                    height_grid[i][j] = 0
                    visible_value = grid[i][j]
                else:
                    height_grid[i][j] = visible_value - grid[i][j]
        return height_grid

    def get_min_grid(self, grid_1, grid_2):
        source_height = len(grid_1)
        source_width = len(grid_2[0])
        min_grid = [[0 for _ in range(source_height)] for _ in range(source_width)]
        for i in range(source_height):
            for j in range(source_width):
                min_grid[i][j] = min(grid_1[i][j], grid_2[i][j])
        return min_grid


    def my_understanding_maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        source_height = len(grid)
        source_width = len(grid[0])
        rotated_grid = deepcopy(grid)
        min_grid = deepcopy(grid)
        for _ in range(4):
            rotated_grid = self.rotate90CW(rotated_grid)
            solution_grid = self.solve_in_one_direction(rotated_grid)
            min_grid = [[min(min_grid[i][j], solution_grid[i][j]) for j in range(source_height)] for i in range(source_width)]
        return sum([sum(_row) for _row in min_grid])

    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        rows_max = [max(_row) for _row in grid]
        columns_max = [max([grid[i][j] for i in range(height)]) for j in range(width)]
        new_city = [[min(rows_max[i], columns_max[j]) - grid[i][j] for j in range(width)] for i in range(height)]
        return sum([sum(_row) for _row in new_city])



grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
my_solution = Solution()
print(my_solution.maxIncreaseKeepingSkyline(grid))



