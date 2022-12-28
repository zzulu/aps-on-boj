T = int(input())


def is_square(n):
    return int(n ** 0.5) ** 2 == n


for _ in range(T):
    x, y = map(int, input().split())
    distance = y - x

    if int(distance ** 0.5) ** 2 == distance:
        move = int(distance ** 0.5) * 2 - 1
    else:
        move = int(distance ** 0.5) * 2

    if int(distance ** 0.5) ** 2 + int(distance ** 0.5) < distance:
        move += 1
    print(move)


# 1 1
# 2 2
# 3 3
# 4 3
# 5 4
# 6 4
# 7 5
# 8 5
# 9 5
# 10 6
# 11 6
# 12 6
# 13 7
# 14 7
# 15 7
# 16 7
# 17 8
# 18 8
