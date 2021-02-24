from collections import deque
N, K = map(int, input().split())
people = deque([str(n) for n in range(1, N+1)])

result = []
while people:
    people.rotate(-(K-1))
    result.append(people.popleft())

print('{}{}{}'.format('<', ', '.join(result), '>'))
