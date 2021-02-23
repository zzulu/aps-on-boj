import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque([])
commands = {
    'push_front': lambda item: queue.appendleft(item),
    'push_back': lambda item: queue.append(item),
    'pop_front': lambda _: queue.popleft() if queue else '-1',
    'pop_back': lambda _: queue.pop() if queue else '-1',
    'size': lambda _: len(queue),
    'empty': lambda _: '0' if queue else '1',
    'front': lambda _: queue[0] if queue else '-1',
    'back': lambda _: queue[-1] if queue else '-1',
}
for _ in range(N):
    command = sys.stdin.readline().split()
    output = commands[command[0]](command[-1])
    if output is not None: print(output)
