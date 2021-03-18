N = int(input())

count = 0
for x in range(1, N+1):
    number = str(x)
    if len(number) == 1:
        count += 1
    else:
        delta = int(number[0]) - int(number[1])
        for index in range(1, len(number)-1):
            if delta != int(number[index]) - int(number[index+1]):
                break
        else:
            count += 1

print(count)
