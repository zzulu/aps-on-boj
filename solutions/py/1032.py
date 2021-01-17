N = int(input())

file_names = []
for _ in range(N):
    file_names.append(input())

result = ''
for i in range(len(file_names[0])):
    char = file_names[0][i]
    for file_name in file_names[1:]:
        if char != file_name[i]:
            result += '?'
            break
    else:
        result += char

print(result)
