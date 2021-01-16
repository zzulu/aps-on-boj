T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    dp = [[0]*(M+1) for _ in range(N+1)]

    for m in range(1, M+1):
        dp[1][m] = m
    for n in range(2, N+1):
        for m in range(n, M+1):
            for d in range(m-1, 0, -1):
                dp[n][m] += dp[n-1][d]

    print(dp[N][M])
