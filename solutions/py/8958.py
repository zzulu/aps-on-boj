T = int(input())
for _ in range(T):
    score = input()
    current, result = 1, 0
    for s in score:
        if s == 'O':
            result += current
            current += 1
        else:
            current = 1
    print(result)
