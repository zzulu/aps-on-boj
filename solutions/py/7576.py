import sys
from collections import deque


def get_next(m: int, n: int, max_m: int, max_n: int) -> list:
    directions = []
    if n-1 >= 0:
        directions.append((m, n-1))
    if n+1 < max_n:
        directions.append((m, n+1))
    if m-1 >= 0:
        directions.append((m-1, n))
    if m+1 < max_m:
        directions.append((m+1, n))
    return directions


M, N = map(int, input().split())

box = [ [0]*M for _ in range(N) ]

items = []
for n in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    for m in range(M):
        box[n][m] = row[m]
        if row[m] == 1:
            items.append((m, n))

visited = [ [False]*M for _ in range(N) ]

queue = deque([items]) # [[],[],...]

days = 0
while queue:
    items = queue.popleft()

    next_items = []
    for m, n in items:
        if not visited[n][m]:
            visited[n][m] = True
            for next_m, next_n in get_next(m, n, M, N):
                if box[next_n][next_m] == 0 and not visited[next_n][next_m]:
                    box[next_n][next_m] = 1
                    next_items.append((next_m, next_n))

    if next_items:
        queue.append(next_items)
        days += 1

unable = False
for n in range(N):
    for m in range(M):
        if box[n][m] == 0:
            unable = True
            break
    if unable: break

if unable:
    print(-1)
else:
    print(days)
