from typing import *
from enum import Enum
from copy import deepcopy


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
    parent = graph[current.parent]
    ancestors = [parent.id]
    distance_log = 0
    while parent and len(parent.ancestors) > distance_log:
        parent_ind = parent.ancestors[distance_log]
        ancestors.append(parent_ind)
        parent = graph[parent_ind]
        distance_log += 1
    return ancestors


def dfs(graph: List[Vertex], current: Vertex, time: int, dist: int) -> int:
    current.time_in = time
    current.color = Color.GREY
    current.dist = dist
    for son_edge in current.connections:
        son_vertex_id = son_edge.to
        son_vertex = graph[son_vertex_id]
        if son_vertex.color is Color.WHITE:
            son_vertex.parent = current.id
            son_vertex.ancestors = extract_parents(graph, son_vertex)
            time = dfs(graph, graph[son_vertex_id], time+1, dist+son_edge.weight)
    time += 1
    current.time_out = time
    current.color = Color.BLACK
    return time


def dfs_without_recursion(graph: List[Vertex], root: Vertex) -> List[Vertex]:
    stack = []
    root.dist = 0
    root.ancestors = []
    stack.append(root)
    time = -1
    while len(stack) > 0:
        current = stack[-1]
        if current.color is Color.WHITE:
            current.color = Color.GREY
            time += 1
            current.time_in = time
        children = [graph[_s.to] for _s in current.connections]
        weights = {_s.to: _s.weight for _s in current.connections}
        children = list(filter(lambda x: x.color is Color.WHITE, children))
        for son in children:
            stack.append(son)
            son.parent = current.id
            son.dist = current.dist + weights[son.id]
            son.ancestors = extract_parents(graph, son)
        if len(children) == 0:
            time += 1
            current.time_out = time
            current.color = Color.BLACK
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
    current_vertex = from_vertex
    pointer = len(current_vertex.ancestors) - 1
    while pointer >= 0:
        try:
            candidate_ind = current_vertex.ancestors[pointer]
            candidate_vertex = graph[candidate_ind]
            if is_v1_ancestor_for_v2(candidate_vertex, to_vertex):
                pointer -= 1
            else:
                current_vertex = candidate_vertex  # ToDo: иногда нужен сдвиг
                pointer = len(candidate_vertex.ancestors) - 1
        except:
            debug = None
    return candidate_vertex


def get_min_distance(graph: List[Vertex], from_vertex_ind: int, to_vertex_ind: int) -> int:
    from_vertex = graph[from_vertex_ind]
    to_vertex = graph[to_vertex_ind]
    lca = get_lca(graph, from_vertex, to_vertex)
    distance = from_vertex.dist + to_vertex.dist - 2 * lca.dist
    return distance


def solve():
    n = int(input())
    graph = [Vertex(i) for i in range(n)]

    for _ in range(n - 1):
        u, v, w = map(int, input().strip().split())
        graph[u].connections.append(Edge(v, w))
        graph[v].connections.append(Edge(u, w))

    m = int(input())

    ROOT = graph[0]
    graph = dfs_without_recursion(graph, ROOT)

    for _ in range(m):
        from_ind, to_ind = map(int, input().strip().split())
        min_distance = get_min_distance(graph, from_ind, to_ind)
        print(min_distance)


if __name__ == "__main__":
    solve()
