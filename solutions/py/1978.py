N = int(input())
numbers = list(map(int, input().split()))
prime = [0 for _ in range(1001)]

for number in numbers:
    prime[number] = 1

prime[1] = 0
for n in range(2, int(1000**0.5)+1):
    number = n + n
    while number < 1001:
        prime[number] = 0
        number += n

print(sum(prime))
