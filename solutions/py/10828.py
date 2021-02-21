import sys
N = int(sys.stdin.readline())
stack = []
commands = {
    'push': lambda item: stack.append(item),
    'pop': lambda _: stack.pop() if stack else '-1',
    'size': lambda _: len(stack),
    'empty': lambda _: '0' if stack else '1',
    'top': lambda _: stack[-1] if stack else '-1',
}
for _ in range(N):
    command = sys.stdin.readline().split()
    output = commands[command[0]](command[-1])
    if output is not None: print(output)


# import sys
# N = int(sys.stdin.readline())
# stack = [-1] + [None]*10000
# index = 0
# for _ in range(N):
#     command = sys.stdin.readline().split()
#     if command[0] == 'push':
#         index += 1
#         stack[index] = command[1]
#     elif command[0] == 'pop':
#         print(stack[index])
#         if index:
#             index -= 1
#     elif command[0] == 'size':
#         print(index)
#     elif command[0] == 'empty':
#         print(1) if not index else print(0)
#     elif command[0] == 'top':
#         print(stack[index])
