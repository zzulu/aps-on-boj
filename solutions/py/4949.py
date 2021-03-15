brackets = {')': '(', ']': '['}
line = input()
while line != '.':
    stack = []
    for char in line:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets:
            if stack and stack[-1] == brackets[char]:
                stack.pop()
            else:
                print('no')
                break
    else:
        if not stack:
            print('yes')
        else:
            print('no')

    line = input()
