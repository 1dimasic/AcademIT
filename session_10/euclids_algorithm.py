def get_greatest_common_divisor(number_1, number_2):
    if number_2 == 0:
        return number_1

    return get_greatest_common_divisor(number_2, number_1 % number_2)


first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))

if first_number == 0 and second_number == 0:
    print('Наибольший общий делитель найти нельзя')
else:
    greatest_common_divisor = get_greatest_common_divisor(first_number, second_number)
    print(f'Наибольший общий делитель = {greatest_common_divisor}')
