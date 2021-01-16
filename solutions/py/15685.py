N = int(input())
board = [[0]*101 for _ in range(101)]
delta = ((0, 1), (-1, 0), (0, -1), (1, 0))
rect = 0

for _ in range(N):
    x, y, d, g = map(int, input().split())

    route = [d]
    for _ in range(g):
        for r in route[::-1]:
            route.append((r+1)%4)

    board[y][x] = 1
    for r in route:
        y += delta[r][0]
        x += delta[r][1]
        board[y][x] = 1

for y in range(100):
    for x in range(100):
        if board[y][x] and board[y+1][x] and board[y][x+1] and board[y+1][x+1]:
            rect += 1

print(rect)
