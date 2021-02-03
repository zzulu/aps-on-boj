def toggle(s):
    return '0' if s == '1' else '1'

N = int(input())
switches = ['']+input().split()
S = int(input())
for _ in range(S):
    g, i = map(int, input().split())

    if g == 1:
        step = i
        while i < len(switches):
            switches[i] = toggle(switches[i])
            i += step
    else:
        switches[i] = toggle(switches[i])
        l, r = i-1, i+1
        while 0 < l and r < len(switches) and switches[l] == switches[r]:
            switches[l] = toggle(switches[l])
            switches[r] = toggle(switches[r])
            l -= 1
            r += 1

line = ((N-1)//20)+1
for l in range(line):
    print(' '.join(switches[20*l+1:20*l+21]))
