L = int(input())
ad = input()

pi = [0] * L

begin = 0
for index in range(1, L):
    while (begin > 0 and ad[index] != ad[begin]):
        begin = pi[begin-1]
    
    if (ad[index] == ad[begin]):
        begin += 1
        pi[index] = begin

print(L-pi[-1])
