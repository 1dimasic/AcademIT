start_number = int(input('Введите начальное значение: '))
end_number = int(input('Введите конечное значение: '))
numbers_in_line_count = int(input('Введите количество чисел в одной строке: '))

i = start_number
printed_numbers_in_line_count = 0
number_width = len(str(end_number))

while i <= end_number:
    if printed_numbers_in_line_count == numbers_in_line_count:
        print()
        printed_numbers_in_line_count = 0

    print('%*d' % (number_width, i), end=' ')

    printed_numbers_in_line_count += 1
    i += 1
