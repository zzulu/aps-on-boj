N, X, K = input().split()
for _ in range(int(K)):
    a, b = input().split()
    if X == a:
        X = b
    elif X == b:
        X = a
print(X)
