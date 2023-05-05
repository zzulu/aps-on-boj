import sys
from collections import deque


def get_next(m: int, n: int, h:int, max_m: int, max_n: int, max_h: int) -> list:
    directions = []
    if n-1 >= 0:
        directions.append((m, n-1, h))
    if n+1 < max_n:
        directions.append((m, n+1, h))
    if m-1 >= 0:
        directions.append((m-1, n, h))
    if m+1 < max_m:
        directions.append((m+1, n, h))
    if h-1 >= 0:
        directions.append((m, n, h-1))
    if h+1 < max_h:
        directions.append((m, n, h+1))
    return directions


M, N, H = map(int, input().split())

box = [[ [0]*M for _ in range(N) ] for _ in range(H)]

items = []
for h in range(H):
    for n in range(N):
        line = list(map(int, sys.stdin.readline().split()))
        for m in range(M):
            box[h][n][m] = line[m]
            if line[m] == 1:
                items.append((m, n, h))

visited = [[ [False]*M for _ in range(N) ] for _ in range(H)]

queue = deque([items]) # [[],[],...]

days = 0
while queue:
    items = queue.popleft()

    next_items = []
    for m, n, h in items:
        if not visited[h][n][m]:
            visited[h][n][m] = True
            for next_m, next_n, next_h in get_next(m, n, h, M, N, H):
                if box[next_h][next_n][next_m] == 0 and not visited[next_h][next_n][next_m]:
                    box[next_h][next_n][next_m] = 1
                    next_items.append((next_m, next_n, next_h))

    if next_items:
        queue.append(next_items)
        days += 1

unable = False
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 0:
                unable = True
                break
        if unable: break
    if unable: break

if unable:
    print(-1)
else:
    print(days)
