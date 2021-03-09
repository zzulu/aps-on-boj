def d(n):
    for d in str(n):
        n += int(d)
    return n

numbers = [True for n in range(10000)]
for n in range(1, 10001):
    n = d(n)
    while n <= 10000:
        numbers[n-1] = False
        n = d(n)

for number, self_n in enumerate(numbers):
    if self_n:
        print(number+1)
