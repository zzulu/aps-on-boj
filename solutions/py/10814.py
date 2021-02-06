N = int(input())
members = []
for _ in range(N):
    members.append(input().split())

members.sort(key=lambda m: int(m[0]))
for member in members:
    print(' '.join(member))
