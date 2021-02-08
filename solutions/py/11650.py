N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
points.sort()
for point in points:
    print(point[0], point[1])

