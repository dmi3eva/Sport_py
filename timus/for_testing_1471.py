from typing import *
from enum import Enum
import sys


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
        self.ancestors: Optional[List[int]] = []
        self.connections: List[Edge] = []
        self.color: Color = Color.WHITE
        self.parent: Optional[int] = None


def extract_parents(graph: List[Vertex], current: Vertex) -> List[int]:
    parent_ind = graph[current.parent].id
    ancestors = [parent_ind]
    distance_log = 0
    while graph[parent_ind] and len(graph[parent_ind].ancestors) > distance_log:
        parent_ind = graph[parent_ind].ancestors[distance_log]
        ancestors.append(parent_ind)
        distance_log += 1
    return ancestors


def dfs_without_recursion(graph: List[Vertex], root: Vertex) -> List[Vertex]:
    stack: List[int]
    stack = []
    root.dist = 0
    root.ancestors = []
    stack.append(root.id)
    time = -1
    while len(stack) > 0:
        current = stack[-1]
        if graph[current].color is Color.WHITE:
            graph[current].color = Color.GREY
            time += 1
            graph[current].time_in = time
        children = [(_s.to, _s.weight) for _s in graph[current].connections]
        children = list(filter(lambda x: graph[x[0]].color is Color.WHITE, children))
        for son in children:
            stack.append(son[0])
            graph[son[0]].parent = graph[current].id
            graph[son[0]].dist = graph[current].dist + son[1]
            graph[son[0]].ancestors = extract_parents(graph, graph[son[0]])
        if len(children) == 0:
            time += 1
            graph[current].time_out = time
            graph[current].color = Color.BLACK
            stack.pop()
    return graph


def is_v1_ancestor_for_v2(vertex_1: Vertex, vertex_2: Vertex) -> bool:
    time_in_condition = vertex_1.time_in < vertex_2.time_in
    time_out_condition = vertex_1.time_out > vertex_2.time_out
    return time_in_condition and time_out_condition


def get_lca(graph: List[Vertex], from_vertex: Vertex, to_vertex: Vertex) -> Vertex:
    if from_vertex.id == to_vertex.id:
        return from_vertex
    if is_v1_ancestor_for_v2(from_vertex, to_vertex):
        return from_vertex
    if is_v1_ancestor_for_v2(to_vertex, from_vertex):
        return to_vertex
    if len(from_vertex.ancestors) < len(to_vertex.ancestors):
        current_vertex_id = from_vertex.id
        finish_id = to_vertex.id
    else:
        current_vertex_id = to_vertex.id
        finish_id = from_vertex.id
    pointer = len(graph[current_vertex_id].ancestors) - 1
    while pointer >= 0:
        candidate_id = graph[current_vertex_id].ancestors[pointer]
        if is_v1_ancestor_for_v2(graph[candidate_id], graph[finish_id]):
            pointer -= 1
        else:
            current_vertex_id = candidate_id
            pointer = len(graph[candidate_id].ancestors) - 1
    return graph[candidate_id]


def get_min_distance(graph: List[Vertex], from_vertex_ind: int, to_vertex_ind: int) -> int:
    from_vertex = graph[from_vertex_ind]
    to_vertex = graph[to_vertex_ind]
    lca = get_lca(graph, from_vertex, to_vertex)
    distance = from_vertex.dist + to_vertex.dist - 2 * lca.dist
    return distance


def solve():
    n = int(sys.stdin.readline())
    graph = [Vertex(i) for i in range(n)]
    for i in range(n - 1):
        line = sys.stdin.readline()
        u, v, w = map(int, line.split())
        graph[u].connections.append(Edge(v, w))
        graph[v].connections.append(Edge(u, w))

    m = int(sys.stdin.readline())
    ranges = [None for _ in range(m)]
    for i in range(m):
        ranges[i] = sys.stdin.readline()


    ROOT = graph[0]
    graph = dfs_without_recursion(graph, ROOT)

    for range_to_find in ranges:
        s, f = map(int, range_to_find.split())
        min_distance = get_min_distance(graph, s, f)
        print(min_distance)


if __name__ == "__main__":
    solve()