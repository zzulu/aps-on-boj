N, T, C, P = map(int, input().split())
print((N//T)*C*P) if N%T else print((N//T-1)*C*P)
