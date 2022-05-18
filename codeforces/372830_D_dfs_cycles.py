from enum import Enum
from typing import *


class Color(Enum):
    WHITE = 0
    GREY = 1
    BLACK = 2


class Vertex:
    def __init__(self, vertex_id: int):
        self.id: int = vertex_id
        self.color: Color = Color.WHITE
        self.parent: Optional[int] = None
        self.connections: List[int] = []


def dfs(current: Vertex, graph: List[Vertex], time: int) -> bool:
    current.color = Color.GREY
    result = False
    for neighbor in current.connections:
        if graph[neighbor].color is Color.WHITE:
            graph[neighbor].parent = current.id
            result = dfs(graph[neighbor], graph, time + 1)
            if result:
                return True
        if graph[neighbor].color is Color.GREY and current.parent != neighbor:
            return True
    current.color = Color.BLACK
    return result


def solve() -> NoReturn:
    n, m = map(int, input().strip().split())
    graph = [Vertex(i) for i in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().strip().split())
        graph[a].connections.append(b)
        graph[b].connections.append(a)

    for v in graph[1:]:
        if v.color is not Color.WHITE:
            continue
        result = dfs(v, graph, 0)
        if result:
            print("YES")
            return
    print("NO")

if __name__ == "__main__":
    solve()