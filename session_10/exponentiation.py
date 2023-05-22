def get_exponentiation_v_1(degree_base, exponent):
    if exponent == 0:
        return 1

    return get_exponentiation_v_1(degree_base, exponent - 1) * degree_base


def get_exponentiation_v_2(degree_base, exponent):
    result = 1

    for i in range(1, exponent + 1):
        result *= degree_base

    return result


degree_base_a = int(input('Введите основание степени а: '))
exponent_n = int(input('Введите показатель степени n > 0: '))

if exponent_n < 0:
    print('Показатель степени должен быть больше 0')
else:
    print(f'{degree_base_a} в степени {exponent_n} = {get_exponentiation_v_1(degree_base_a, exponent_n)}')
    print(f'{degree_base_a} в степени {exponent_n} = {get_exponentiation_v_2(degree_base_a, exponent_n)}')
