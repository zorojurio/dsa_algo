

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def __str__(self):
        return f'{self.adjacency_list}'

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            return True
        return False

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        return False

    def remove_edge(self, vertex1, vertex2):
        try:
            if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
                return True
            return False
        except ValueError as e:
            print(e)
            return False


if __name__ == '__main__':
    custom_graph = Graph()
    custom_graph.add_vertex('a')
    custom_graph.add_vertex('b')
    custom_graph.add_vertex('c')
    custom_graph.add_vertex('d')
    custom_graph.add_edge('a', 'b')
    custom_graph.add_edge('b', 'c')
    custom_graph.add_edge('c', 'a')
    print(custom_graph)
    custom_graph.remove_edge('a', 'd')
    # custom_graph.remove_edge('b', 'c')
    # custom_graph.remove_edge('c', 'a')
    print(custom_graph)
