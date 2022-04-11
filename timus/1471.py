from typing import *
from enum import Enum


class Color(Enum):
    WHITE = 0
    GREY = 1
    BLACK = 2


class Edge:
    def __init__(self, to: int, weight: int):
        self.to: int = to
        self.weight: int = weight


class Vertex:
    def __init__(self, id):
        self.id: int = id
        self.dist: Optional[int] = None
        self.time_in: Optional[int] = None
        self.time_out: Optional[int] = None
        self.parents: Optional[List] = None
        self.connections: List[Edge] = []
        self.color = Color.WHITE


def dfs(graph: List[Vertex], current: Vertex, time: int, dist: int, parent: Optional[int]) -> int:
    current.time_in = time
    current.color = Color.GREY
    current.dist = dist
    current.parents = None
    for son_edge in current.connections:
        son_vertex_id = son_edge.to
        son_vertex = graph[son_vertex_id]
        if son_vertex.color is Color.WHITE:
            time = dfs(graph, graph[son_vertex_id], time+1, dist+son_edge.weight, parents+[current.id])
    time += 1
    current.time_out = time
    current.color = Color.BLACK
    return time


n = int(input())
graph = [Vertex(i) for i in range(n)]

for _ in range(n - 1):
    u, v, w = map(int, input().split())
    graph[u].connections.append(Edge(v, w))
    graph[v].connections.append(Edge(u, w))

ROOT = graph[0]
_ = dfs(graph, ROOT, 0, 0, [])
a = 7