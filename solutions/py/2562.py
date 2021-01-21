index, max_num = 0, 0
for i in range(9):
    num = int(input())
    if num > max_num:
        index, max_num = i, num

print(max_num)
print(index+1)
