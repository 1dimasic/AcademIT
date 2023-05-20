import math

radius = 5
circle_length = 2.0 * math.pi * radius
circle_area = math.pi * pow(radius, 2)
print('Длина окружности: {:.2f}, площадь круга: {:.2f}'.format(circle_length, circle_area))

circle_area = 78.54
radius = math.sqrt(circle_area / math.pi)
print('Радиус: {:.2f}'.format(radius))

radius = 5
angle = 30
sector_area = math.pi * pow(radius, 2) * angle / 360.0
print('Площадь сектора: {:.2f}'.format(sector_area))
