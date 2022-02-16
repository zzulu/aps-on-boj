from collections import deque

N, M, K = map(int, input().split())
gym = [list(input()) for n in range(N)]
x1, y1, x2, y2 = map(int, input().split())

visited = [[N*M] * M for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

queue = deque([(x1-1,y1-1)])
visited[x1-1][y1-1] = 0
while queue:
    x, y = queue.popleft()

    for d in range(4):
        next_x, next_y = x+dx[d], y+dy[d]
        next_k = 1
        while (0 <= next_x < N and 0 <= next_y < M) and gym[next_x][next_y] == '.' and next_k <= K and visited[next_x][next_y] > visited[x][y]:
            if visited[next_x][next_y] == N*M:
                queue.append((next_x, next_y))
                visited[next_x][next_y] = visited[x][y] + 1
            next_x += dx[d]
            next_y += dy[d]
            next_k += 1

print(-1) if visited[x2-1][y2-1] == N*M else print(visited[x2-1][y2-1])
