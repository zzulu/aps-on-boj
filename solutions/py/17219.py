import sys

N, M = map(int, sys.stdin.readline().split())

storage = {}
for _ in range(N):
    url, password = sys.stdin.readline().split()
    storage[url] = password

for _ in range(M):
    target = sys.stdin.readline().rstrip()
    print(storage[target])
