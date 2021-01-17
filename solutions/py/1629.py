def pow(a, b, c):
    if not b:
        return 1

    n = pow(a, b//2, c)
    if b % 2:
        return (n * n * a) % c
    else:
        return (n * n) % c

a, b, c = map(int, input().split())
print(pow(a, b, c))
