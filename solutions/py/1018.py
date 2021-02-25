N, M = map(int, input().split())
board = [input() for _ in range(N)]
color = ['', 'W', 'B']

min_count = 64
for y in range(N-7):
    for x in range(M-7):
        start_w, start_b = 0, 0
        current = 1
        for dy in range(8):
            for dx in range(8):
                if board[y+dy][x+dx] != color[current]:
                    start_w += 1
                if board[y+dy][x+dx] != color[current*(-1)]:
                    start_b += 1
                current *= (-1)
            current *= (-1)

        count = min(start_w, start_b)
        if count < min_count:
            min_count = count

print(min_count)
