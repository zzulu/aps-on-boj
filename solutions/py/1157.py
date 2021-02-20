word = input()
count = {}
for char in word:
    if count.get(char.upper()):
        count[char.upper()] += 1
    else:
        count[char.upper()] = 1

result = sorted(count.items(), key=lambda item: item[1])[-2:]
if len(result) < 2 or result[-1][1] > result[-2][1]:
    print(result[-1][0])
else:
    print('?')
