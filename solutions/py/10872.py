N = int(input())

if N:
    result = 1
    for n in range(1, N+1):
        result *= n
    print(result)
else:
    print(1)
