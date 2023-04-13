import sys
from math import ceil
def input():
    return sys.stdin.readline().rstrip()

N, H_ATK = map(int, input().split())

H_MaxHP = 0
H_CurHP = 0

for _ in range(N):
    t, a, h = map(int, input().split())

    if t == 1:
        H_turn = ceil(h / H_ATK)
        H_CurHP -= a * (H_turn-1)
    else: # t == 2
        H_ATK += a
        H_CurHP += h

    if H_CurHP > 0:
        H_CurHP = 0

    H_MaxHP = max(H_MaxHP, abs(H_CurHP))

print(H_MaxHP+1)
