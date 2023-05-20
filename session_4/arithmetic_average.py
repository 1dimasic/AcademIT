# Вариант 1
start_number = 3
end_number = 17

numbers_sum = 0
numbers_count = 0
even_numbers_sum = 0
even_numbers_count = 0

i = start_number

while i <= end_number:
    numbers_sum += i
    numbers_count += 1

    if i % 2 == 0:
        even_numbers_sum += i
        even_numbers_count += 1

    i += 1

arithmetic_average = numbers_sum / numbers_count
even_numbers_arithmetic_average = even_numbers_sum / even_numbers_count
print(f'Среднее арифметическое чисел из диапазона [{start_number};{end_number}] равно {arithmetic_average},'
      f' среднее арифметическое четных чисел равно {even_numbers_arithmetic_average}')

# Вариант 2
numbers_list = [x for x in range(start_number, end_number + 1)]
even_numbers_list = [x for x in range(start_number, end_number + 1) if x % 2 == 0]

arithmetic_average = sum(numbers_list) / len(numbers_list)
even_numbers_arithmetic_average = sum(even_numbers_list) / len(even_numbers_list)
print(f'Среднее арифметическое чисел из диапазона [{start_number};{end_number}] равно {arithmetic_average},'
      f' среднее арифметическое четных чисел равно {even_numbers_arithmetic_average}')
