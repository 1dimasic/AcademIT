numbers_count = int(input('Введите количество чисел ряда: '))

i = 1
numbers_sum = 0

while i <= numbers_count:
    if i % 2 != 0:
        numbers_sum += i ** 2
    else:
        numbers_sum -= i ** 2

    i += 1

print(f'Сумма ряда = {numbers_sum}')

# Вариант 2
numerical_series = [x ** 2 if x % 2 != 0 else -x ** 2 for x in range(1, numbers_count + 1)]
print(f'Сумма ряда = {sum(numerical_series)}')
