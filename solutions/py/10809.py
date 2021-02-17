S = input()
position = ['-1']*26
for index, char in enumerate(S):
    if position[ord(char)-97] == '-1':
        position[ord(char)-97] = str(index)
print(' '.join(position))
