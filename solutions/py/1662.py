S = input()

count, K = 0, ''
stack = [[], []]
for s in S:
    if s == '(':
        stack[0].append(count-1)
        stack[1].append(K)
        count, K = 0, ''
    elif s == ')':
        stack[0][-1] += count * stack[1].pop()
        count = stack[0].pop()
    else:
        count += 1
        K = int(s)

print(count)
