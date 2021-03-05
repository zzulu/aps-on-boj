N = int(input())
five, r = N // 5, N % 5
while five > -1:
    three, r = r // 3, r % 3
    if not r:
        break
    five -= 1
    r += three*3 + 5

print(five+three) if five > -1 else print(-1)
