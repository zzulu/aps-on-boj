from collections import deque

N, M, V = map(int, input().split())

graph = [ [] for _ in range(N+1) ]

for _ in range(M):
    f, t = map(int, input().split())
    graph[f].append(t)
    graph[t].append(f)

# DFS
stack = [V]
visited = [False]*(N+1)
result = []

while stack:
    vertex = stack.pop()

    if not visited[vertex]:
        visited[vertex] = True
        result.append(vertex)

        temp = []
        for v in graph[vertex]:
            if not visited[v]:
                temp.append(v)
        temp.sort(reverse=True)

    stack.extend(temp)

print(' '.join(map(str, result)))


# BFS
queue = deque([V])
visited = [False]*(N+1)
result = []

while queue:
    vertex = queue.popleft()

    if not visited[vertex]:
        visited[vertex] = True
        result.append(vertex)

        temp = []
        for v in graph[vertex]:
            if not visited[v]:
                temp.append(v)
        temp.sort()

    queue.extend(temp)

print(' '.join(map(str, result)))
