def z(n, y, x, r, c):
    if n == 1:
        return 0
    if y <= r < y+(n//2) and x <= c < x+(n//2):
        return z(n//2, y, x, r, c)
    if y <= r < y+(n//2) and x+(n//2) <= c < x+n:
        return ((n//2)**2)*1 + z(n//2, y, x+(n//2), r, c)
    if y+(n//2) <= r < y+n and x <= c < x+(n//2):
        return ((n//2)**2)*2 + z(n//2, y+(n//2), x, r, c)
    if y+(n//2) <= r < y+n and x+(n//2) <= c < x+n:
        return ((n//2)**2)*3 + z(n//2, y+(n//2), x+(n//2), r, c)


N, r, c = map(int, input().split())
print(z(2**N, 0, 0, r, c))
