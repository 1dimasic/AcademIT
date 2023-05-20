print('Таблица умножения в диапазоне [первый множитель; последний множитель]')

start_number = int(input('Введите первый множитель: '))
end_number = int(input('Введите последний множитель: '))

if start_number > end_number:
    start_number, end_number = end_number, start_number

max_width = len(str(end_number * end_number))
column_width = len(str(end_number))

print(' ' * (column_width + 1), end=' ')

for table_header in range(start_number, end_number + 1):
    print('%*d' % (max_width, table_header), end=' ')

line_under_table_header = column_width + 1 + (end_number - start_number + 1) * (max_width + 1)
print('\n' + '_' * line_under_table_header)

for multiplier_1 in range(start_number, end_number + 1):
    print('%*d|' % (column_width, multiplier_1), end=' ')

    for multiplier_2 in range(start_number, end_number + 1):
        product = multiplier_1 * multiplier_2
        print('%*d' % (max_width, product), end=' ')

    print()
