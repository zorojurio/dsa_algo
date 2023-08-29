from collections import defaultdict
from typing import List


class Graph:
    def __init__(self, number_of_vertices):
        self.graph = defaultdict(list)
        self.number_of_vertices = number_of_vertices

    def __str__(self):
        return f'Number of Vertices: {self.number_of_vertices} \n{self.graph}'

    def add_edge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topological_sort_util(self, vertex: str, visited: List, stack: List) -> None:
        visited.append(vertex)

        for adjacency_vertex in self.graph[vertex]:
            if adjacency_vertex not in visited:
                self.topological_sort_util(adjacency_vertex, visited, stack)
        stack.insert(0, vertex)

    def topological_sort(self):
        visited = []
        stack = []

        for vertex in list(self.graph):
            if vertex not in visited:
                self.topological_sort_util(vertex, visited, stack)
        print(stack)


if __name__ == '__main__':
    graph = Graph(8)
    graph.add_edge("A", "C")
    graph.add_edge("F", "G")
    graph.add_edge("B", "D")
    graph.add_edge("B", "C")
    graph.add_edge("D", "F")
    graph.add_edge("C", "E")
    graph.add_edge("E", "H")
    graph.add_edge("E", "F")

    graph.topological_sort()
    print(graph)
