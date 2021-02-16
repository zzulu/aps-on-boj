N, X = map(int, input().split())
numbers = map(int, input().split())
result = []
for number in numbers:
    if number < X:
        result.append(str(number))
print(' '.join(result))
