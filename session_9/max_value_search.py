def get_max(numbers_list):
    max_number = numbers_list[0]

    for number in numbers_list:
        if number > max_number:
            max_number = number

    return max_number


numbers = [2.5, -2.9, 3, -90.8]

print(f'Максимальное число в списке = {get_max(numbers)}')
