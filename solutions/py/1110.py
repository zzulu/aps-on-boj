N = int(input())
number, count = N, 0
while True:
    count += 1
    number = int(str(number%10)+str((number//10+number%10)%10))
    if N == number: break
print(count)
