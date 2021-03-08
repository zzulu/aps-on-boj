C = int(input())
for tc in range(C):
    s = list(map(int, input().split()))
    students, scores = s[0], s[1:]
    avg = sum(scores)/students
    count = 0
    for score in scores:
        if score > avg:
            count += 1
    print('{:.3f}%'.format(round((count/students)*100, 3)))
