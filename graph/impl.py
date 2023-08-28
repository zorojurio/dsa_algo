class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def __str__(self):
        return f'{self.gdict}'

    def __repr__(self):
        return f'{self.gdict}'

    def add_edge(self, vertex, edge):
        self.gdict[vertex].append(edge)


if __name__ == '__main__':
    data = {
        'a': ['b', 'c'],
        'b': ['a', 'd', 'e'],
        'c': ['a', 'e'],
        'd': ['d', 'e', 'f'],
        'e': ['d', 'f'],
        'f': ['d', 'e'],
    }

    graph = Graph(gdict=data)
    graph.add_edge('e', 'b')
    graph.add_edge('e', 'c')
    print(graph)
