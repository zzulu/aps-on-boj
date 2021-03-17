import sys
N = int(sys.stdin.readline())

points = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))

points.sort(key=lambda point: (point[1], point[0]))

for point in points:
    print(f'{point[0]} {point[1]}')
