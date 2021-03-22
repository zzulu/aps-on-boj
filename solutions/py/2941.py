word = input()
length = len(word)
for c in ('c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='):
    length -= word.count(c)
print(length)
