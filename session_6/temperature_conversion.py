def get_kelvin_temperature(celsius):
    return celsius + 273.15


def get_fahrenheit_temperature(celsius):
    return celsius * 1.8 + 32


celsius_temperature = float(input('Введите температуру в градусах Цельсия: '))
print(f'Температура в градусах Кельвина = {get_kelvin_temperature(celsius_temperature)}')
print(f'Температура в градусах Фаренгейта = {get_fahrenheit_temperature(celsius_temperature):.2f}')
