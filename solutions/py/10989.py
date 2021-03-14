import sys
N = int(sys.stdin.readline())
numbers = [0 for _ in range(10001)]
for i in range(N):
    numbers[int(sys.stdin.readline())] += 1
for i in range(1, 10001):
    for _ in range(numbers[i]):
        print(i)
