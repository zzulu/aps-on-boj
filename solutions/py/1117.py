W, H, f, c, x1, y1, x2, y2 = map(int, input().split())
div = min(W-f, f)

colored = 0
if div <= x1:
    colored += x2-x1
elif x1 < div <= x2:
    colored += (div-x1)*2 + (x2-div)
else:
    colored += (x2-x1)*2

colored *= (y2-y1) * (c+1)

print(W*H - colored)
