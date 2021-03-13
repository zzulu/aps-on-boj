L = int(input())
s = input()
result = 0
for i in range(L):
    result += ((ord(s[i])-96)*(31**i))%1234567891
print(result%1234567891)
