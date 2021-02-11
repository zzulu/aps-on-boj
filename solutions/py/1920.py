T = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
numbers = map(int, input().split())


def binary_search(A, start, end, number):
    if start > end:
        return 0

    center = (start+end)//2

    if number == A[center]:
        return 1

    if number < A[center]:
        return binary_search(A, start, center-1, number)
    else:
        return binary_search(A, center+1, end, number)


for number in numbers:
    print(binary_search(A, 0, len(A)-1, number))
