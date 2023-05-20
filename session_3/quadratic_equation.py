import math

# Уравнение вида a*x*x + b*x + c = 0
a = float(input('Введите коэффициент а = '))
b = float(input('Введите коэффициент b = '))
c = float(input('Введите коэффициент c = '))

epsilon = 0.0001

if math.isclose(a, 0, abs_tol=epsilon):
    if math.isclose(b, 0, abs_tol=epsilon):
        if math.isclose(c, 0, abs_tol=epsilon):
            print('Корнем уравнения является любое число')
        else:
            print('Корней нет')
    else:
        x_1 = -c / b
        print(f'Корень уравнения x = {x_1}')
else:
    discriminant = pow(b, 2) - 4 * a * c

    if math.isclose(discriminant, 0, abs_tol=epsilon):
        x_1 = -b / (2 * a)
        print(f'Корень уравнения x = {x_1}')
    elif discriminant < -epsilon:
        print('Корней нет')
    else:
        x_1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x_2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f'Корни уравнения: x1 = {x_1:.2f}, x2 = {x_2:.2f}')
