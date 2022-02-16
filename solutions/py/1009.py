# def modulo(a, b, m):
#     if b < 2:
#         return a ** b % m

#     if b % 2:
#         return (modulo(a, (b // 2) + 1, m) * modulo(a, b // 2 , m)) % m
    
#     return (modulo(a, b // 2, m) * modulo(a, b // 2, m)) % m


# n = int(input())
# for _ in range(n):
#     a, b = map(int, input().split())
#     print(modulo(a, b, 10))


numbers = {
    0: [10],
    1: [1],
    2: [2, 4, 8, 6],
    3: [3, 9, 7, 1],
    4: [4, 6],
    5: [5],
    6: [6],
    7: [7, 9, 3, 1],
    8: [8, 4, 2, 6],
    9: [9, 1],
}

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    a = a % 10
    
    x = 1
    if a in (2, 3, 7, 8):
        x = 4
    elif a in (4, 9):
        x = 2

    print(numbers[a][(b-1)%x])
