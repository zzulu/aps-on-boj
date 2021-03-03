N = int(input())
for n in range(1, N):
    if N == n+sum(map(int, list(str(n)))):
        print(n)
        break
else:
    print(0)
