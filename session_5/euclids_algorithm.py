number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))

if number_1 == 0 and number_2 == 0:
    print('Наибольший общий делитель найти нельзя')
else:
    while number_2 != 0:
        number_1, number_2 = number_2, number_1 % number_2

    print(f'Наибольший общий делитель = {number_1}')
