def get_3x_plus_4y(x, y):
    return 3 * x + 4 * y


def get_average(begin, end):
    numbers_sum = 0
    numbers_count = 0

    for i in range(begin, end + 1):
        numbers_sum += i
        numbers_count += 1

    return numbers_sum / numbers_count


def get_max(x, y):
    if x > y:
        return x

    return y


def get_min(x, y):
    if x < y:
        return x

    return y


print(get_3x_plus_4y(2, 4))
print(get_average(5, 10))
print(get_min(5, 5))
print(get_max(2, 6))
