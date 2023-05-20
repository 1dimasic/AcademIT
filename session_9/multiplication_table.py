def print_multiplication_table_v_1(first, last):
    max_width = len(str(last * last))
    multiplication_table = []

    for multiplier_1 in range(first, last + 1):
        multiplication_table_string = []

        for multiplier_2 in range(first, last + 1):
            multiplication_table_string.append(multiplier_1 * multiplier_2)

        multiplication_table.append(multiplication_table_string)

    for string in range(len(multiplication_table)):
        for product in multiplication_table[string]:
            print('%*d' % (max_width, product), end=' ')

        print()


def print_multiplication_table_v_2(first, last):
    multiplication_table = [[multiplier_1 * multiplier_2 for multiplier_1 in range(first, last + 1)]
                            for multiplier_2 in range(first, last + 1)]

    for string in multiplication_table:
        print(string)

    print()


print('Таблица умножения в диапазоне [первый множитель; последний множитель]')

start_number = int(input('Введите первый множитель: '))
end_number = int(input('Введите последний множитель: '))

if start_number > end_number:
    start_number, end_number = end_number, start_number

print_multiplication_table_v_1(start_number, end_number)
print()
print_multiplication_table_v_2(start_number, end_number)
