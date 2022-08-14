T = int(input())

for _ in range(T):
    N = int(input())
    numbers = {n: 1 for n in input().split()}
    M = int(input())
    for m in input().split():
        print(numbers.get(m, 0))
