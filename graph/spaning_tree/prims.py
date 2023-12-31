from collections import defaultdict
import heapq


def create_spanning_tree(graph, starting_vertex):
    mst = defaultdict(set)
    visited = {starting_vertex}
    edges = [(cost, starting_vertex, to) for to, cost in graph[starting_vertex].items()]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst[frm].add(to)
            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next))
    return mst


example_graph = {
    'A': {'C': 3, 'B': 2},
    'B': {'A': 2, 'C': 1, 'D': 1, 'E': 4},
    'C': {'A': 3, 'B': 1, 'F': 5},
    'D': {'B': 1, 'E': 1},
    'E': {'B': 4, 'D': 1, 'F': 1},
    'F': {'C': 5, 'E': 1, 'G': 1},
    'G': {'F': 1},
}

print(dict(create_spanning_tree(example_graph, 'A')))
# second test
graph_two = {
    'A': {'B': 5, 'C': 13, 'E': 15},
    'B': {'A': 5, 'C': 10, 'D': 8},
    'C': {'A': 13, 'B': 10, 'E': 20, 'D': 6},
    'D': {'B': 8, 'C': 6},
    'E': {'A': 15, 'C': 20}
}
print(dict(create_spanning_tree(graph_two, 'A')))
