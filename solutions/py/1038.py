N = int(input())

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
index = 0

if N < 10:
    print(N)
elif N > 1022:
    print(-1)
else:
    while True:
        prev = numbers[index] % 10
        for p in range(prev):
            numbers.append(numbers[index] * 10 + p)

        if len(numbers) > N:
            print(numbers[N])
            break

        index += 1
