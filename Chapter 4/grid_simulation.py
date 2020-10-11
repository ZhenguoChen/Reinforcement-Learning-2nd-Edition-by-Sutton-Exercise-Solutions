import pandas as pd
from copy import deepcopy

size = 4
grid = [[0 for i in range(size)] for i in range(size)]

def update(grid):
    gamma = 0.9
    old_grid = deepcopy(grid)

    def valid_pos(i, j):
        return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i == 0 and j == 0) or (i == len(grid)-1 and j == len(grid[0])-1):
                continue
            grid[i][j] = sum([
                gamma * old_grid[next_i][next_j]
                if valid_pos(next_i, next_j) else gamma * old_grid[i][j]
                for next_i, next_j in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            ])/4 - 1
    return grid

def show_grid(grid):
    print(pd.DataFrame(grid))

for i in range(100):
    grid = update(grid)
    show_grid(grid)
