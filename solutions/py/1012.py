def get_udlr(x: int, y: int, max_x: int, max_y: int) -> list:
    result = []
    if y-1 >= 0:
        result.append((x, y-1))
    if y+1 < max_y:
        result.append((x, y+1))
    if x-1 >= 0:
        result.append((x-1, y))
    if x+1 < max_x:
        result.append((x+1, y))
    return result


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    ground = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]

    items = []
    for _ in range(K):
        X, Y = map(int, input().split())
        items.append((X, Y))
        ground[Y][X] = 1

    count = 0
    for start_x, start_y in items:
        if visited[start_y][start_x]:
            continue

        count += 1
        stack = [(start_x, start_y)]

        while stack:
            x, y = stack.pop()
            if not visited[y][x]:
                visited[y][x] = True
                for next_x, next_y in get_udlr(x, y, M, N):
                    if ground[next_y][next_x] and not visited[next_y][next_x]:
                        stack.append((next_x, next_y))

    print(count)
