import math

print('Введите координаты точки А.')
x_1 = float(input('Координата x = '))
y_1 = float(input('Координата y = '))

print('Введите координаты точки B.')
x_2 = float(input('Координата x = '))
y_2 = float(input('Координата y = '))

print('Введите координаты точки C.')
x_3 = float(input('Координата x = '))
y_3 = float(input('Координата y = '))

epsilon = 0.001

if math.isclose(x_3 * (y_2 - y_1) - x_1 * (y_2 - y_3), x_2 * (y_3 - y_1), abs_tol=epsilon):
    print("Все три точки A, B и С лежат на одной прямой!")
else:
    # вычисляем длину сторон треугольника a, b, c
    a = math.sqrt(pow(x_1 - x_2, 2) + pow(y_1 - y_2, 2))
    b = math.sqrt(pow(x_2 - x_3, 2) + pow(y_2 - y_3, 2))
    c = math.sqrt(pow(x_3 - x_1, 2) + pow(y_3 - y_1, 2))

    perimeter_half = (a + b + c) / 2.0

    area = math.sqrt(perimeter_half * (perimeter_half - a) * (perimeter_half - b) * (perimeter_half - c))
    print('Площадь треугольника равна %.2f' % area)
