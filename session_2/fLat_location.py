import math

entrances_count = int(input('Введите количество подъездов: '))
floors_count = int(input('Введите количество этажей: '))
flat_number = int(input('Введите номер квартиры: '))

flats_on_floor_count = 4

""" Проверка условия вхождения
номера квартиры в доме"""
if entrances_count * floors_count * flats_on_floor_count < flat_number or flat_number < 0:
    print('Такой квартиры не существует!')
else:
    entrance_number = math.ceil(flat_number / (floors_count * flats_on_floor_count))  # находим номер подъезда
    # находим номер этажа
    floor_number = math.ceil(
        (flat_number - (entrance_number - 1) * floors_count * flats_on_floor_count) / flats_on_floor_count)
    flat_location = flat_number % flats_on_floor_count  # находим положение квартиры на этаже
    print('Номер подъезда: %s\nЭтаж: %s' % (entrance_number, floor_number))

    if flat_location == 1:
        print('Ближняя слева')
    elif flat_location == 2:
        print('Дальняя слева')
    elif flat_location == 3:
        print('Дальняя справа')
    else:
        print('Ближняя справа')
