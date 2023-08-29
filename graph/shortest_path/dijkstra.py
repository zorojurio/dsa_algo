import heapq
from typing import List


class Edge:
    def __init__(self, weight, start_vertex, target_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.target_vertex = target_vertex

    def __str__(self) -> str:
        return (
            f"{self.weight} \n"
            f"{self.start_vertex} \n"
            f"{self.target_vertex} \n"
        )


class Node:
    def __init__(self, name: str) -> None:
        self.name = name
        self.visited: bool = False
        self.predecessor = None
        self.neighbours: List = []
        self.min_distance = float("inf")

    def add_edge(self, weight, destination_vertex):
        edge = Edge(
            weight=weight,
            start_vertex=self,
            target_vertex=destination_vertex
        )
        self.neighbours.append(edge)

    def __lt__(self, other):
        return self.min_distance < other.min_distance

    def __str__(self):
        return (
            f"{self.name} \n"
            f"{self.visited} \n"
            f"{self.predecessor} \n"
            f"{self.neighbours} \n"
            f"{self.min_distance} \n"
        )


class Dijkstra:
    def __init__(self):
        self.heap = []

    def calculate(self, start_vertex: Node):
        start_vertex.min_distance = 0
        # TODO: check the return value
        heapq.heappush(self.heap, start_vertex)
        while self.heap:
            # pop element with the lowest distance
            actual_vertex: Node = heapq.heappop(self.heap)
            if actual_vertex.visited:
                continue
            # consider neighbours
            for edge in actual_vertex.neighbours:
                start: Node = edge.start_vertex
                target: Node = edge.target_vertex
                new_distance = start.min_distance + edge.weight
                if new_distance < target.min_distance:
                    target.min_distance = new_distance
                    target.predecessor = start
                    # update heap
                    heapq.heappush(self.heap, target)
            actual_vertex.visited = True

    # start_vertex provided in calculate
    @staticmethod
    def get_shortest_path(vertex: Node):
        print(f'Shortest path to the {vertex.name} is {vertex.min_distance}')
        actual_vertex = vertex
        while actual_vertex:
            print(actual_vertex.name, end=" ")
            actual_vertex = actual_vertex.predecessor
        print()


if __name__ == '__main__':
    # step 1 create nodes
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    f = Node('F')
    g = Node('G')
    h = Node('H')

    # step 2 - create edges
    a.add_edge(6, b)
    a.add_edge(9, d)
    a.add_edge(10, c)

    b.add_edge(5, d)
    b.add_edge(12, f)
    b.add_edge(16, e)

    c.add_edge(6, d)
    c.add_edge(5, h)
    c.add_edge(21, g)

    d.add_edge(8, f)
    d.add_edge(7, h)

    e.add_edge(10, g)

    f.add_edge(4, e)
    f.add_edge(12, g)

    h.add_edge(2, f)
    h.add_edge(14, g)

    algo = Dijkstra()
    algo.calculate(a)
    algo.get_shortest_path(f)
    algo.get_shortest_path(g)
