T = int(input())

for _ in range(T):
    n = input()
    r = str(int(n) + int(n[::-1]))
    if r == r[::-1]:
        print("YES")
    else:
        print("NO")
