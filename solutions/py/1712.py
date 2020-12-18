a, b, c = list(map(int, input().split()))
d = c - b

if d > 0:
    print(a//d + 1)
else:
    print(-1)
