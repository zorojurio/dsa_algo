class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = []
        self.nodes = []

    def add_edge(self, start, destination, weight):
        self.graph.append([start, destination, weight])

    def add_node(self, value):
        self.nodes.append(value)

    @staticmethod
    def print_solution(dist):
        print('Vertex distance from Source')
        for key, value in dist.items():
            print(' ' + key + ': ', value)

    def bellman_ford(self, src):
        dist = {i: float('inf') for i in self.nodes}
        dist[src] = 0

        for _ in range(self.v-1):
            for start, destination, weight in self.graph:
                if dist[start] != float('inf') and dist[start] + weight < dist[destination]:
                    dist[destination] = dist[start] + weight

        for start, destination, weight in self.graph:
            if dist[start] != float('inf') and dist[start] + weight < dist[start]:
                print('Graph Contains a negative cycle')
                return

        self.print_solution(dist)


if __name__ == '__main__':
    g = Graph(5)
    g.add_node("A")
    g.add_node("B")
    g.add_node("C")
    g.add_node("D")
    g.add_node("E")
    g.add_edge("A", "C", 6)
    g.add_edge("A", "D", 6)
    g.add_edge("B", "A", 3)
    g.add_edge("C", "D", 1)
    g.add_edge("D", "C", 2)
    g.add_edge("D", "B", 1)
    g.add_edge("E", "B", 4)
    g.add_edge("E", "D", 2)
    g.bellman_ford("B")
