from typing import List

INF = float('inf')

graph_ = [
    [0, 8, INF, 1],
    [INF, 0, 1, INF],
    [4, INF, 0, INF],
    [INF, 2, 9, 1]
]


def print_graph(graph: List[List], num_vectors: int):
    for i in range(num_vectors):
        for k in range(num_vectors):
            if graph[i][k] == INF:
                print('INF', end=' ')
            else:
                print(graph[i][k], end=' ')
        print()


print_graph(graph=graph_, num_vectors=4)


def floyd_warshall(graph: List[List], num_vectors: int):
    for via_vertex in range(num_vectors):
        for i in range(num_vectors):
            for k in range(num_vectors):
                graph[i][k] = min(graph[i][k],  graph[i][via_vertex] + graph[via_vertex][k])

    print_graph(graph, num_vectors)


print('Floyd Warshall All Pair Shortest Path')
floyd_warshall(graph=graph_, num_vectors=4)
