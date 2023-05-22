def get_greatest_common_divisor(number_1, number_2):
    if number_1 == 0 and number_2 == 0:
        return -1

    if number_2 == 0:
        return number_1

    return get_greatest_common_divisor(number_2, number_1 % number_2)


greatest_common_divisor = get_greatest_common_divisor(int(input('Введите первое число: ')),
                                                      int(input('Введите второе число: ')))

if greatest_common_divisor == -1:
    print('Наибольший общий делитель найти нельзя')
else:
    print(f'Наибольший общий делитель = {greatest_common_divisor}')
