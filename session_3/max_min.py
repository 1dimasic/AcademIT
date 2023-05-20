number_1 = int(input('Введите первое число = '))
number_2 = int(input('Введите второе число = '))

if number_1 == number_2:
    print('Числа равны')
elif number_1 > number_2:
    print('Наибольшее число = %s, наименьшее число = %s' % (number_1, number_2))
else:
    print('Наибольшее число = %s, наименьшее число = %s' % (number_2, number_1))

if number_1 == number_2:
    print('Числа равны')
else:
    max_number = number_1 if number_1 > number_2 else number_2
    min_number = number_1 if number_1 < number_2 else number_2
    print(f'Наибольшее число = {max_number}, наименьшее число = {min_number}')
