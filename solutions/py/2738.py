N, M = map(int, input().split())
A, B = [], []

for _ in range(N):
    A.append(list(map(int, input().split())))

for n in range(N):
    B_row = list(map(int, input().split()))
    for m in range(M):
        A[n][m] += B_row[m]

for n in range(N):
    print(' '.join(map(str, A[n])))
