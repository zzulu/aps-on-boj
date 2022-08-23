vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

s = input()
while s != '#':
    count = 0
    for c in s:
        if c in vowels:
            count += 1
    print(count)
    s = input()
