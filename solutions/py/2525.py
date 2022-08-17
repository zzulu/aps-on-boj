A, B = map(int, input().split())
C = int(input())

H, M = (A+((B+C)//60))%24, (B+C)%60
print(f'{H} {M}')
