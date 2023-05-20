limit_upper_number = int(input('Введите целое число, ограничивающее сверху последовательность простых чисел: '))

print(f'Простые числа, не превышающие {limit_upper_number}: ', end='')

for number in range(2, limit_upper_number + 1):
    max_divider = number // 2

    for divider in range(2, max_divider + 1):
        if number % divider == 0:
            break
    else:
        print(number, end=' ')
