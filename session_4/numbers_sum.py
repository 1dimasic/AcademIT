# Сумма чисел от 0 до 9
i = 0
numbers_sum = 0

while i <= 9:
    numbers_sum += i
    i += 1

print(f'Сумма от 0 до 9 равна {numbers_sum}')

# Сумма чисел от 3 до 21
i = 3
numbers_sum = 0

while i <= 21:
    numbers_sum += i
    i += 1

print(f'Сумма от 3 до 21 равна {numbers_sum}')

# Сумма четных чисел от 3 до 21 и их количество
i = 3
even_numbers_count = 0
even_numbers_sum = 0

while i <= 21:
    if i % 2 == 0:
        even_numbers_sum += i
        even_numbers_count += 1

    i += 1

print(f'Сумма четных чисел от 3 до 21 равна {even_numbers_sum}, их количество {even_numbers_count}')
