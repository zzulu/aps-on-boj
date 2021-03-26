L, P = map(int, input().split())
print(' '.join([str(int(n)-(L*P)) for n in input().split()]))
