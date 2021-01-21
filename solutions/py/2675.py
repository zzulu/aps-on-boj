T = int(input())
for _ in range(T):
    R, S = input().split()
    result = ''
    for s in S:
        result += s*int(R)
    print(result)
