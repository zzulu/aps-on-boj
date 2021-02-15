A = int(input())
B = int(input())
C = int(input())
number = str(A*B*C)
count = {}
for n in number:
    if count.get(n):
        count[n] += 1
    else:
        count[n] = 1

for n in range(10):
    print(count.get(str(n), 0))
