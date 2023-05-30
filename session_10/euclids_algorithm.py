def get_greatest_common_divisor(_number_1, _number_2):
    if _number_2 == 0:
        return _number_1

    return get_greatest_common_divisor(_number_2, _number_1 % _number_2)


number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))

if number_1 == 0 and number_2 == 0:
    print('Наибольший общий делитель найти нельзя')
else:
    greatest_common_divisor = get_greatest_common_divisor(number_1, number_2)
    print(f'Наибольший общий делитель = {greatest_common_divisor}')
