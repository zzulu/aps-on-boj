from itertools import combinations


def get_next(y, x, n, m):
    d = [[1, 0],[0, 1],[-1, 0],[0, -1]]
    return [(y+dy, x+dx) for dy, dx in d if (0 <= y+dy and y+dy < n) and (0 <= x+dx and x+dx < m)]

N, M = map(int, input().split())

board = []

for _ in range(N):
    board.append(list(map(int, input().split())))


def dfs(start_y, start_x, depth, parent_y, parent_x): # return sum of numbers
    if depth <= 1:
        return board[start_y][start_x]
    else:
        sum_list = []
        for ny, nx in get_next(start_y, start_x, N, M):
            if parent_y == ny and parent_x == nx:
                continue
            sum = dfs(ny, nx, depth-1, start_y, start_x)
            sum_list.append(sum)

    if depth == 3:
        next_list = [(ny, nx) for ny, nx in get_next(start_y, start_x, N, M) if parent_y != ny or parent_x != nx]

        for a, b in combinations(next_list, 2):
            sum = board[a[0]][a[1]] + board[b[0]][b[1]]
            sum_list.append(sum)

    return board[start_y][start_x] + max(sum_list)


max_sum = 0

for y in range(N):
    for x in range(M):
        sum = dfs(y, x, 4, None, None)
        if sum > max_sum:
            max_sum = sum

print(max_sum)
