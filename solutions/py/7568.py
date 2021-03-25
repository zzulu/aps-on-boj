N = int(input())
people = [tuple(map(int, input().split())) for _ in range(N)]
result = [1 for _ in range(N)]
for i in range(N):
    for person in people:
        if person[0] > people[i][0]  and person[1] > people[i][1]:
            result[i] += 1
print(' '.join(map(str, result)))
