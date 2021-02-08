N = int(input())
two, five = 0, 0
for n in range(2, N+1):
    q = n
    q, r = q//2, q%2
    while not r:
        two += 1
        q, r = q//2, q%2

    q = n
    q, r = q//5, q%5
    while not r:
        five += 1
        q, r = q//5, q%5

print(min(two, five))
