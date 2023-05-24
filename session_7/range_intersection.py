from range import Range


def get_min(point_1, point_2):
    if point_1 < point_2:
        return point_1

    return point_2


def get_max(point_1, point_2):
    if point_1 > point_2:
        return point_1
    
    return point_2


range_1_start_point = float(input('Введите начало первого интервала: '))
range_1_end_point = float(input('Введите конец первого интервала: '))

range_2_start_point = float(input('Введите начало второго интервала: '))
range_2_end_point = float(input('Введите конец второго интервала: '))

range_1 = Range(range_1_start_point, range_1_end_point)
range_2 = Range(range_2_start_point, range_2_end_point)

min_end_point = get_min(range_1_end_point, range_2_end_point)

if range_1.is_inside(range_2.start):
    print(f'Интервалы пересекаются, область пересечения = [{range_2.start};{min_end_point}]')
elif range_2.is_inside(range_1.start):
    print(f'Интервалы пересекаются, область пересечения = [{range_1.start};{min_end_point}]')
else:
    print('Интервалы не пересекаются')
    betweens_range = Range(get_min(range_1.end, range_2.end), get_max(range_1.start, range_2.start))
    print(f'Расстояние между двумя интервалами = {betweens_range.get_length()}')
