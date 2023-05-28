def get_even_numbers_arithmetic_average(numbers_list):
    even_numbers_sum = 0
    even_numbers_count = 0

    for number in numbers_list:
        if number % 2 == 0:
            even_numbers_sum += number
            even_numbers_count += 1

    return even_numbers_sum / even_numbers_count


values_list = [2, 3, 5, -6, 8, 9, 10, 0]
print(f'Среднее арифметическое четных чисел списка = {get_even_numbers_arithmetic_average(values_list)}')
