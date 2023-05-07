import sys

N, M = map(int, sys.stdin.readline().split())

graph = [ [] for _ in range(N+1) ]
visited = [False]*(N+1)
visited[0] = True

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

result = 0
current = 1
while not all(visited):
    result += 1
    while visited[current]:
        current += 1

    stack = [current]

    while stack:
        vertex = stack.pop()
        visited[vertex] = True
        for v in graph[vertex]:
            if not visited[v]:
                stack.append(v)

print(result)
