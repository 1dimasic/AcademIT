def get_max(values_list):
    max_value = values_list[0]

    for value in values_list:
        if value > max_value:
            max_value = value

    return max_value


numbers_list = [2.5, -2.9, 3, -90.8]

print(f'Максимальное значение в списке = {get_max(numbers_list)}')
