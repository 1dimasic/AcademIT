string = '1,2,3,4,5'

numbers_strings = string.split(',')
numbers_sum = 0

for number_string in numbers_strings:
    numbers_sum += int(number_string)

print(f'Сумма чисел в строке "{string}" = {numbers_sum}')
