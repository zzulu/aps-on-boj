from sys import maxsize


def dijkstra(start: int, graph: list) -> list:
    N = len(graph)-1
    vertex = start

    visited = [False]*(N+1)
    times = [maxsize]*(N+1)

    visited[vertex] = True
    times[vertex] = 0

    while vertex:
        for v, t in graph[vertex]:
            times[v] = min(times[v], times[vertex]+t)

        min_index, min_time = 0, maxsize
        for index, time in enumerate(times):
            if not visited[index] and time < min_time:
                min_index, min_time = index, time

        vertex = min_index
        visited[vertex] = True

    return times


N, M, X = map(int, input().split())

graph = [ [] for _ in range(N+1) ]
reverse_graph = [ [] for _ in range(N+1) ]

for _ in range(M):
    start, end, T = map(int, input().split())
    graph[start].append((end, T))
    reverse_graph[end].append((start, T))

forward = dijkstra(X, graph)
reverse = dijkstra(X, reverse_graph)

result = [forward[n] + reverse[n] for n in range(1, N+1)]

print(max(result))
