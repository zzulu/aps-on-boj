A, B = map(int, input().split())

numbers = [0]
n = 0
for n in range(46):
    for _ in range(n):
        numbers.append(n)

print(sum(numbers[A:B+1]))
