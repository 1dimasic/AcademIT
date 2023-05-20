from range import Range


def get_min(first_point, second_point):
    if first_point < second_point:
        return first_point
    return second_point


def get_max(first_point, second_point):
    if first_point > second_point:
        return first_point
    return second_point


first_range_start_point = float(input('Введите начало первого интервала: '))
first_range_end_point = float(input('Введите конец первого интервала: '))

second_range_start_point = float(input('Введите начало второго интервала: '))
second_range_end_point = float(input('Введите конец второго интервала: '))

first_range = Range(first_range_start_point, first_range_end_point)
second_range = Range(second_range_start_point, second_range_end_point)

min_end_point = get_min(first_range_end_point, second_range_end_point)

if first_range.is_inside(second_range.start):
    print(f'Интервалы пересекаются, область пересечения = [{second_range.start};{min_end_point}]')
elif second_range.is_inside(first_range.start):
    print(f'Интервалы пересекаются, область пересечения = [{first_range.start};{min_end_point}]')
else:
    print('Интервалы не пересекаются')
    betweens_range = Range(get_min(first_range.end, second_range.end), get_max(first_range.start, second_range.start))
    print(f'Расстояние между двумя интервалами = {betweens_range.get_length()}')
