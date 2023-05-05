X = int(input())
d = [0]*(X+1)

for n in range(2, X+1):
    d[n] = d[n-1] + 1
    if n % 3 == 0:
        d[n] = min(d[n], d[n//3]+1)
    if n % 2 == 0:
        d[n] = min(d[n], d[n//2]+1)

print(d[X])
