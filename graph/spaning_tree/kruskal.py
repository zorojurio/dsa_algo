from graph.spaning_tree.disjoint import DisjointSet


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []
        self.nodes = []
        self.minimum_spanning_tree = []

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    def add_node(self, value):
        self.nodes.append(value)

    def print_solution(self):
        for s, d, w in self.minimum_spanning_tree:
            print("%s - %s: %s" % (s, d, w))

    def kruskal_algo(self):
        i_th_edge, no_edges_spanned = 0, 0
        ds = DisjointSet(self.nodes)
        self.graph = sorted(self.graph, key=lambda item: item[2])
        while no_edges_spanned < self.vertices - 1:
            start, destination, weight = self.graph[i_th_edge]
            i_th_edge += 1
            x_parent = ds.find(start)
            y_parent = ds.find(destination)
            if x_parent != y_parent:
                # if parents are different, it is not a cyclic relationship
                no_edges_spanned += 1
                self.minimum_spanning_tree.append([start, destination, weight])
                ds.union(x_parent, y_parent)
        self.print_solution()


g = Graph(5)
g.add_node("A")
g.add_node("B")
g.add_node("C")
g.add_node("D")
g.add_node("E")
g.add_edge("A", "B", 5)
g.add_edge("A", "C", 13)
g.add_edge("A", "E", 15)
g.add_edge("B", "A", 5)
g.add_edge("B", "C", 10)
g.add_edge("B", "D", 8)
g.add_edge("C", "A", 13)
g.add_edge("C", "B", 10)
g.add_edge("C", "E", 20)
g.add_edge("C", "D", 6)
g.add_edge("D", "B", 8)
g.add_edge("D", "C", 6)
g.add_edge("E", "A", 15)
g.add_edge("E", "C", 20)

g.kruskal_algo()
