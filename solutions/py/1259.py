number = input()
while number != '0' :
    if number == number[::-1]:
        print('yes')
    else:
        print('no')
    number = input()
