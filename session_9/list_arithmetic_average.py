numbers = [2, 3, 5, -6, 8, 9, 10, 0]

even_numbers_sum = 0
even_numbers_count = 0

for even_numbers_count, even_number in enumerate(element for element in numbers if element % 2 == 0):
    even_numbers_sum += even_number

arithmetic_average = even_numbers_sum / (even_numbers_count + 1)

print(f'Среднее арифметическое списка = {arithmetic_average}')
