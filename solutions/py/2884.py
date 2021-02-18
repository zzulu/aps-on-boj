h, m = map(int, input().split())
if m-45 < 0: h -= 1
h, m = h%24, (m-45)%60
print('{} {}'.format(h, m))
