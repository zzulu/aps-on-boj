T = int(input())

for _ in range(T):
    points = []
    for _ in range(4):
        points.append(tuple(map(int, input().split())))

    distances = []
    for i in range(4):
        for j in range(i+1, 4):
            distances.append((points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2)

    print(1) if len(set(distances)) == 2 else print(0)
