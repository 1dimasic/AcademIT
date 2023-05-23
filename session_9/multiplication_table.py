def creat_multiplication_table_v_1(first_multiplier, last_multiplier):
    table = []

    for multiplier_1 in range(first_multiplier, last_multiplier + 1):
        table_row = []

        for multiplier_2 in range(first_multiplier, last_multiplier + 1):
            table_row.append(multiplier_1 * multiplier_2)

        table.append(table_row)

    return table


def creat_multiplication_table_v_2(first_multiplier, last_multiplier):
    table = [[multiplier_1 * multiplier_2 for multiplier_1 in range(first_multiplier, last_multiplier + 1)]
             for multiplier_2 in range(first_multiplier, last_multiplier + 1)]

    return table


def print_multiplication_table(table, last_multiplier):
    max_width = len(str(last_multiplier * last_multiplier))

    for row in range(len(table)):
        for product in table[row]:
            print('%*d' % (max_width, product), end=' ')

        print()

    print()


print('Таблица умножения в диапазоне [первый множитель; последний множитель]')

start_number = int(input('Введите первый множитель: '))
end_number = int(input('Введите последний множитель: '))

if start_number > end_number:
    start_number, end_number = end_number, start_number

multiplication_table = creat_multiplication_table_v_1(start_number, end_number)
print_multiplication_table(multiplication_table, end_number)

multiplication_table = creat_multiplication_table_v_2(start_number, end_number)
print_multiplication_table(multiplication_table, end_number)
