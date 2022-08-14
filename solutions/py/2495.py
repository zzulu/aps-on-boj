for _ in range(3):
    number = input()
    current, count, max_number = number[0], 1, 1
    for n in number[1:]:
        if current == n:
            count += 1
        else:
            if count > max_number:
                max_number = count
            current, count = n, 1
    print(max(max_number, count))
