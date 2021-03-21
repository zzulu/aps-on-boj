N = int(input())

count = 0
for _ in range(N):
    word = input()
    alphabets = ['']
    for char in word:
        if char != alphabets[-1]:
            if char not in alphabets:
                alphabets.append(char)
            else:
                break
    else:
        count += 1

print(count)
