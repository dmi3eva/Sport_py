import sys
from typing import *
from enum import Enum
sys.setrecursionlimit(900)


class Cell(Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2


def dfs(x: int, y: int, n: int, area: List[List[Cell]]) -> bool:
    if x == n and y == 2:
        return True
    delta_x = [0, -1, 1]
    delta_y = [0, -1, 1]
    area[y][x] = Cell.GRAY
    for dx in delta_x:
        for dy in delta_y:
            if area[y + dy][x + dx] is Cell.WHITE:
                if dfs(x + dx, y + dy, n, area):
                    return True
    return False


t = int(input())
for _ in range(t):
    n = int(input())
    level = [[Cell.BLACK for _ in range(n+2)]]
    for _row in range(2):
        line = input()
        new_row = [Cell.BLACK] + [Cell.WHITE if _c == '0' else Cell.BLACK for _c in line] + [Cell.BLACK]
        level.append(new_row)
    level.append([Cell.BLACK for _ in range(n + 2)])
    result = dfs(1, 1, n, level)
    if result:
        print("YES")
    else:
        print("NO")