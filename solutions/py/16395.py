"""
16395. 파스칼의 삼각형
"""

def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n-1)

n, k = list(map(int, input().split()))
print(fact(n-1)//(fact(k-1)*fact(n-k)))