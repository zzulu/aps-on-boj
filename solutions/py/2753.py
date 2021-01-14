year = int(input())
print('1') if (not year % 4 and year % 100) or not year % 400 else print('0')
