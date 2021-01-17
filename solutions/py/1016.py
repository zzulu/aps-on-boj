l, r = map(int, input().split())

numbers = [1 for n in range(r-l+1)]
for i in range(2, int(r**0.5)+1):
    n = i**2
    for j in range((l//n)*n, r+1, n):
        if j >= l and numbers[j-l]:
            numbers[j-l] = 0

print(sum(numbers))
