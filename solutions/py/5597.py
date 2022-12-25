students = {n: 1 for n in range(1, 31)}

for _ in range(28):
    students[int(input())] -= 1

for s in filter(lambda s: s[1], students.items()):
    print(s[0])
