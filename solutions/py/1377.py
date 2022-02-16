import sys

N = int(input())
A = [(int(sys.stdin.readline()), n) for n in range(N)]
A_sorted = sorted(A)

result = 0
for n in range(N):
    if result < A_sorted[n][1] - A[n][1]:
        result = A_sorted[n][1] - A[n][1]

print(result+1)
