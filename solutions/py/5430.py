from collections import deque


def run_p(p: str, n: int, l: list) -> str:
    left = True
    queue = deque(l)
    for f in p:
        if f == 'R':
            left = not left
        elif f == 'D':
            if n <= 0:
                return 'error'
            if left:
                queue.popleft()
            else:
                queue.pop()
            n -= 1
    if not left:
        queue.reverse()
    return f"[{','.join(queue)}]"


T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    l = input()[1:-1].split(',')
    print(run_p(p, n, l))
