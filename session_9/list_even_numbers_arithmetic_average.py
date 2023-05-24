def get_arithmetic_average(array):
    even_numbers_sum = 0
    even_numbers_count = 0

    for number in array:
        if number % 2 == 0:
            even_numbers_sum += number
            even_numbers_count += 1

    even_numbers_arithmetic_average = even_numbers_sum / even_numbers_count

    return even_numbers_arithmetic_average


numbers = [2, 3, 5, -6, 8, 9, 10, 0]
print(f'Среднее арифметическое четных чисел списка = {get_arithmetic_average(numbers)}')
