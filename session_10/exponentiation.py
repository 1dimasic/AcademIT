def raise_to_power_with_recursion(number, power):
    if power == 0:
        return 1

    return raise_to_power_with_recursion(number, power - 1) * number


def raise_to_power_with_cycle(number, power):
    result = 1

    for i in range(1, power + 1):
        result *= number

    return result


number_a = int(input('Введите основание степени а: '))
power_n = int(input('Введите показатель степени n > 0: '))

if power_n < 0:
    print('Показатель степени должен быть больше 0')
else:
    print(f'{number_a} в степени {power_n} = {raise_to_power_with_recursion(number_a, power_n)}')
    print(f'{number_a} в степени {power_n} = {raise_to_power_with_cycle(number_a, power_n)}')
