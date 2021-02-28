import sys
T = int(sys.stdin.readline())
for tc in range(1, T+1):
    A, B = map(int, sys.stdin.readline().split())
    print('Case #{}: {}'.format(tc, A+B))
