import re

T = int(input())

regexp = re.compile(r'^(100+1+|01)+$')

for _ in range(T):
    s = input()

    if regexp.search(s):
        print('YES')
    else:
        print('NO')
