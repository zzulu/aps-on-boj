T = int(input())
for _ in range(T):
    stack = []
    PS = input()
    for char in PS:
        if stack and char == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                print('NO')
                break
        else:
            stack.append(char)
    else:
        if not stack:
            print('YES')
        else:
            print('NO')
