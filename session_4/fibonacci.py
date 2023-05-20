number_index = int(input('Введите порядковый номер числа ряда Фибоначчи: '))

if number_index < 0:
    print(f'Число {number_index} меньше 0 !')
elif number_index == 0:
    print(f'Число ряда Фибоначчи с порядковым номером {number_index} = 0')
else:
    previous_fibonacci_number = 0
    current_fibonacci_number = 1
    i = 2

    while i <= number_index:
        previous_fibonacci_number, current_fibonacci_number = \
            current_fibonacci_number, previous_fibonacci_number + current_fibonacci_number
        i += 1

    print(f'Число ряда Фибоначчи с порядковым номером {number_index} = {current_fibonacci_number}')
