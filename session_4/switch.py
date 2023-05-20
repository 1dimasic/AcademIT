number_1 = float(input('Введите первое число: '))
number_2 = float(input('Введите второе число: '))
command_code = input('Введите код команды от 1 до 4: ')
# Работаем со строкой, таким образом исключаем ошибки функции int(), если введено не число

match command_code:
    case '1':
        print(f'Сумма двух чисел равна {number_1 + number_2}')
    case '2':
        print(f'Разность двух чисел равна {number_1 - number_2}')
    case '3':
        print(f'Произведение двух чисел равно {number_1 * number_2}')
    case '4':
        print(f'Частное двух чисел равно {number_1 / number_2:.2f}')
    case _:
        print('Неизвестная операция')
