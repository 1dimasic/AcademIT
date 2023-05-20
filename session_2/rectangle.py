length = float(input('Введите длину прямоугольника: '))
width = float(input('Введите ширину прямоугольника: '))

area = length * width
perimeter = 2 * (length + width)

print('У прямоугольника длина = {0:.2f}, ширина = {1:.2f}, периметр = {2:.2f}, '
      'площадь = {3:.2f}'.format(length, width, perimeter, area))
