def get_greatest_common_divisor(number_1, number_2):
    if number_2 == 0:
        return number_1

    return get_greatest_common_divisor(number_2, number_1 % number_2)


entered_number_1 = int(input('Введите первое число: '))
entered_number_2 = int(input('Введите второе число: '))

if entered_number_1 == 0 and entered_number_2 == 0:
    print('Наибольший общий делитель найти нельзя')
else:
    greatest_common_divisor = get_greatest_common_divisor(entered_number_1, entered_number_2)
    print(f'Наибольший общий делитель = {greatest_common_divisor}')
