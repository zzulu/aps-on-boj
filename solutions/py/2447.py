N = int(input())


def draw(n: int):
    if n == 1:
        return ['*']

    stars = draw(n//3)

    result = []

    for star in stars:
        result.append(star*3)

    for star in stars:
        result.append(star + ' '*(n//3) + star)

    for star in stars:
        result.append(star*3)

    return result


print('\n'.join(draw(N)))
