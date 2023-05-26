class Range:
    def __init__(self, start, end):
        if start > end:
            start, end = end, start

        self.__start = start
        self.__end = end

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, start):
        self.__start = start

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, end):
        self.__end = end

    def get_length(self):
        return self.__end - self.__start

    def is_inside(self, point):
        return self.__start <= point <= self.__end


start_point = float(input('Введите начало интервала: '))
end_point = float(input('Введите конец интервала: '))
point_a = float(input('Введите координату точки А: '))

verifiable_range = Range(start_point, end_point)

if verifiable_range.is_inside(point_a):
    print(f'Точка A находится внутри интервала [{verifiable_range.start} ; {verifiable_range.end}]')
    # создаем два новых объекта экземпляра класса Range
    range_1 = Range(start_point, point_a)
    range_2 = Range(point_a, end_point)
    print(
        f'Расстояние от начала интервала до точки A = {range_1.get_length():.2f}, '
        f'расстояние от точки A до конца интервала = {range_2.get_length():.2f}')
else:
    print(f'Точка А не находится внутри интервала [{verifiable_range.start};{verifiable_range.end}]')

    if point_a < start_point:
        # изменяем значение атрибута start экземпляра segment
        verifiable_range.start = point_a
        print(f'Новый интервал = [{verifiable_range.start};{verifiable_range.end}], '
              f'его длина = {verifiable_range.get_length():.2f}')
    else:
        # изменяем значение атрибута end экземпляра segment
        verifiable_range.end = point_a
        print(
            f'Новый диапазон = [{verifiable_range.start};{verifiable_range.end}], '
            f'его длина = {verifiable_range.get_length():.2f}')
