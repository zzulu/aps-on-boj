for t in range(int(input())):
    h, w, n = [int(i) for i in input().split()]
    a, b = (n%h, (n//h)+1) if n%h else (h, (n//h))
    print('{}{:02}'.format(a, b))
