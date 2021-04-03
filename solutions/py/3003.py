pieces = [1, 1, 2, 2, 2, 8]
print(' '.join((str(pieces[i]-int(n)) for i, n in enumerate(input().split()))))

