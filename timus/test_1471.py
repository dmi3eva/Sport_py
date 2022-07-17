import unittest
from random import randint

from timus.for_testing_1471 import Vertex, Edge, get_min_distance, dfs, dfs_without_recursion
from typing import *

MAX_WEIGHT = 1000


def generate_random_graph(vertex_number: int) -> List[Vertex]:
    graph = [Vertex(i) for i in range(vertex_number)]
    for new_vertex_id in range(1, vertex_number - 1):
        mounting_id = randint(0, new_vertex_id - 1)
        while len(graph[mounting_id].connections) == 3:
            mounting_id = randint(0, new_vertex_id - 1)
        weight = randint(0, MAX_WEIGHT)
        graph[new_vertex_id].connections.append(Edge(mounting_id, weight))
        graph[mounting_id].connections.append(Edge(new_vertex_id, weight))
    return graph


GRAPH_SIZE = 5


class Test1471Solver(unittest.TestCase):
  def setUp(self):
    self.graph = generate_random_graph(GRAPH_SIZE)

  def test_random(self):
    from_id = randint(0, GRAPH_SIZE - 1)
    to_id = randint(0, GRAPH_SIZE - 1)
    # dist = get_min_distance(self.graph, from_id, to_id)
    self.assertRaises(Exception, get_min_distance(self.graph, from_id, to_id))


def test_one_graph(vertex_number: int, experiment_number: int) -> NoReturn:
    graph = generate_random_graph(vertex_number)
    for _ in range(experiment_number):
        from_id = randint(0, vertex_number - 1)
        to_id = randint(0, vertex_number - 1)
        try:
            ROOT = graph[0]
            graph = dfs_without_recursion(graph, ROOT)
            dist = get_min_distance(graph, from_id, to_id)
        except Exception as e:
            print("PROBLEM")
            print(e.with_traceback())
            print(f"from_id = {from_id}:")
            print(f"to_id = {to_id}:")
            for vertex_id in range(vertex_number):
                print(f"{vertex_id}:")
                print(graph[vertex_id].connections)
            print("------------------")
    print("All is OK")


if __name__ == "__main__":
    unittest.main()
