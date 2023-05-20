# Вариант 1
entered_number = input('Введите число: ')

i = 0
digits_sum = 0
odd_digits_sum = 0
max_digit = 0
number = int(entered_number)

while i < len(entered_number):
    digit = number % 10
    digits_sum += digit

    if digit > max_digit:
        max_digit = digit

    if digit % 2 != 0:
        odd_digits_sum += digit

    number //= 10
    i += 1

print(f'В числе {entered_number} сумма цифр = {digits_sum}, сумма нечетных цифр = {odd_digits_sum},'
      f' максимальная цифра = {max_digit}')

# Вариант 2
digits_list = [int(i) for i in entered_number]
odd_digits_list = [int(i) for i in entered_number if int(i) % 2 != 0]

print(f'В числе {entered_number} сумма цифр = {sum(digits_list)}, '
      f'сумма нечетных цифр = {sum(odd_digits_list)},'
      f' максимальная цифра = {max(digits_list)}')

# Вариант 3
i = 0
digits_sum = 0
odd_digits_sum = 0
max_digit = 0

while i < len(entered_number):
    digit = entered_number[i:i + 1]
    digit = int(digit)
    digits_sum += digit

    if digit > max_digit:
        max_digit = digit

    if digit % 2 != 0:
        odd_digits_sum += digit

    i += 1

print(f'В числе {entered_number} сумма цифр = {digits_sum}, сумма нечетных цифр = {odd_digits_sum},'
      f' максимальная цифра = {max_digit}')
