a, b = map(int, input().split())

q, r = a, b
while r != 0:
    q, r = r, q % r

print(q)
print(a*b//q)
