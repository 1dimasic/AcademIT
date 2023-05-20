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

segment = Range(start_point, end_point)

if segment.is_inside(point_a):
    print(f'Точка A находится внутри интервала [{segment.start} ; {segment.end}]')
    # создаем два новых объекта экземпляра класса Range
    first_segment = Range(start_point, point_a)
    second_segment = Range(point_a, end_point)
    print(
        f'Расстояние от начала интервала до точки A = {first_segment.get_length():.2f}, '
        f'расстояние от точки A до конца интервала = {second_segment.get_length():.2f}')
else:
    print(f'Точка А не находится внутри интервала [{segment.start};{segment.end}]')

    if point_a < start_point:
        # изменяем значение атрибута start экземпляра segment
        segment.start = point_a
        print(f'Новый интервал = [{segment.start};{segment.end}], его длина = {segment.get_length():.2f}')
    else:
        # изменяем значение атрибута end экземпляра segment
        segment.end = point_a
        print(f'Новый диапазон = [{segment.start};{segment.end}], его длина = {segment.get_length():.2f}')
