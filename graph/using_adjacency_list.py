from collections import deque


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

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False

    def breath_first_search(self, vertex: str) -> None:
        visited = set()
        visited.add(vertex)
        queue = deque(vertex)
        while queue:
            current_vertex = queue.popleft()
            print(current_vertex)
            for adjacency_vertex in self.adjacency_list[current_vertex]:
                if adjacency_vertex not in visited:
                    visited.add(adjacency_vertex)
                    queue.append(adjacency_vertex)

    def depth_first_search(self, vertex):
        visited = set()  # O(1)
        stack = [vertex]  # O(1)
        while stack:  # o(V)
            current_vertex = stack.pop()  # o(1)
            if current_vertex not in visited:  # o(1)
                print(current_vertex)
                visited.add(current_vertex)
            for adjacency_vertex in self.adjacency_list[current_vertex]:  # O(E) E is number of edges
                if adjacency_vertex not in visited:
                    stack.append(adjacency_vertex)
        # O(V+E)
        # O(V) number of vertices


if __name__ == '__main__':
    custom_graph = Graph()
    custom_graph.add_vertex('a')
    custom_graph.add_vertex('b')
    custom_graph.add_vertex('c')
    custom_graph.add_vertex('d')
    custom_graph.add_vertex('e')
    custom_graph.add_edge('a', 'b')
    custom_graph.add_edge('b', 'e')
    custom_graph.add_edge('c', 'a')
    custom_graph.add_edge('d', 'c')
    custom_graph.add_edge('e', 'd')

    # print(custom_graph)
    # custom_graph.remove_edge('a', 'd')
    # custom_graph.remove_edge('d', 'c')
    # custom_graph.remove_edge('d', 'a')

    # print(custom_graph)
    adjacency_list = {
        'A': ['B', 'C', 'D'],
        'B': ['A', 'C'],
        'C': ['A', 'B', 'D'],
        'D': ['A', 'C']
    }
    # custom_graph.remove_vertex('d')
    # print('After deleting vertex D')
    print(custom_graph)
    custom_graph.breath_first_search('a')
    print('Depth First Search')
    custom_graph.depth_first_search('a')
    # delete vertex of D
