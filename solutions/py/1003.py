def fibonacci(n, memo):
    if memo[n]:
        return memo[n][0], memo[n][1]

    if n == 0: 
        return 1, 0

    if n == 1:
        return 0, 1

    zero, one = tuple(map(sum, zip(fibonacci(n-1, memo), fibonacci(n-2, memo))))
    memo[n] = [zero, one]
    return zero, one


T = int(input())
for _ in range(T):
    N = int(input())
    memo = [None]*41
    zero, one = fibonacci(N, memo)
    print(f'{zero} {one}')
