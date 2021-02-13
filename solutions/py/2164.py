from collections import deque

N = int(input())
cards = [n for n in range(N, 0, -1)]
queue = deque(cards)

while len(queue) > 1:
    queue.pop()
    queue.rotate()

print(queue[0])
