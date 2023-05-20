import math

number_1 = float(input('Введите первое число: '))
number_2 = float(input('Введите второе число: '))

epsilon = 0.0001

if math.isclose(number_1, number_2, abs_tol=epsilon):
    print(f'Числа равны с учетом погрешности epsilon = {epsilon}')
else:
    print('Числа не равны')
