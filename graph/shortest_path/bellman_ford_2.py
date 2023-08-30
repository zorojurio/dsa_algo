from typing import List


class Vertex:
    def __init__(self, name):
        self.name = name
        self.min_distance = float('inf')
        self.prev = None

    def __str__(self):
        return f'{self.name}: {self.min_distance}'


class Edge:
    def __init__(self, start_vertex, destination_vertex, cost):
        self.start_vertex = start_vertex
        self.destination_vertex = destination_vertex
        self.cost = cost

    def __str__(self):
        return f'{self.start_vertex} {self.cost}'


class Graph:
    def __init__(self, size):
        self.edges: List[Edge] = []
        self.size = size

    def __str__(self):
        return f'{[str(edge.start_vertex.name) for edge in self.edges]}'

    def add_edge(self, start_vertex: Vertex, destination_vertex: Vertex, cost: int):
        edge = Edge(
            start_vertex=start_vertex,
            destination_vertex=destination_vertex,
            cost=cost
        )
        self.edges.append(edge)

    def find_paths(self, source_vertex: Vertex):
        source_vertex.min_distance = 0
        for i in range(self.size - 1):
            for edge in self.edges:
                if (edge.start_vertex.min_distance != float('inf') and
                        edge.start_vertex.min_distance + edge.cost < edge.destination_vertex.min_distance):
                    edge.destination_vertex.min_distance = edge.start_vertex.min_distance + edge.cost
                    edge.destination_vertex.prev = edge.start_vertex

        for edge in self.edges:
            if (edge.start_vertex.min_distance != float('inf') and
                    edge.start_vertex.min_distance + edge.cost < edge.destination_vertex.min_distance):
                print('Graph Contains Negative Cycles')
                return False
        return True

    @staticmethod
    def get_shortest_path(destination: Vertex):
        current = destination
        while current:
            print(current.name, end='-> ')
            current = current.prev


if __name__ == '__main__':
    a = Vertex('A')
    b = Vertex('B')
    c = Vertex('C')
    d = Vertex('D')
    e = Vertex('E')
    f = Vertex('F')

    graph = Graph(6)

    graph.add_edge(a, c, 6)
    graph.add_edge(a, c, 6)
    graph.add_edge(b, a, 3)
    graph.add_edge(c, d, 1)
    graph.add_edge(d, c, 2)
    graph.add_edge(d, b, 1)
    graph.add_edge(e, b, 4)
    graph.add_edge(e, d, 2)

    print(graph.find_paths(e))
    print(a.min_distance)
    graph.get_shortest_path(c)
