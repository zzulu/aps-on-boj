while True:
    edges = list(map(int, input().split()))
    if sum(edges) == 0: break
    edges.sort()
    if edges[0]**2 + edges[1]**2 == edges[2]**2:
        print('right')
    else:
        print('wrong')
