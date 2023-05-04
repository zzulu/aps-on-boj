import math

N = int(input())
buildings = list(map(int, input().split()))
counts = [0]*N

for i in range(N):
    left_slope = math.inf
    right_slope = -math.inf
    for j in range(i-1, -1, -1):
        s = (buildings[j]-buildings[i]) / (j-i)
        if s < left_slope:
            left_slope = s
            counts[i] += 1

    for j in range(i+1, N):
        s = (buildings[j]-buildings[i]) / (j-i)
        if s > right_slope:
            right_slope = s
            counts[i] += 1

print(max(counts))
