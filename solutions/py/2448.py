n = 24

def stars(n, lindent=3, rindent=3):
    lines = ['*','* *','*****']
    if n == 3:
        return [' '*(lindent-i)+l+' '*(rindent-i) for i, l in enumerate(lines,start=1)]
    else:
        return stars(n//2, lindent*2, rindent*2) + list(map(lambda x:x[0]+' '+x[1], zip(stars(n//2, lindent*2-3), stars(n//2, rindent=rindent*2-3))))

print('\n'.join(stars(n)))
