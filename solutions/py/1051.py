def square(numbers, N, M):
    L = M if N > M else N
    for l in range(L, -1, -1):
        for y in range(l, N):
            for x in range(l, M):
                if numbers[y-l][x-l] == numbers[y][x-l] == numbers[y-l][x] == numbers[y][x]:
                    return (l+1)**2


N, M = map(int, input().split())
numbers = [[int(n) for n in input()] for _ in range(N)]

print(square(numbers, N, M))
