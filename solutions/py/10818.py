N = int(input())
numbers = map(int, input().split())
min_n, max_n = 1000000, -1000000
for number in numbers:
    if number < min_n:
        min_n = number
    if number > max_n:
        max_n = number

print(min_n, max_n)
