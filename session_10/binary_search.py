def binary_search_with_recursion(array, value, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2

    if array[middle] > value:
        new_right = middle - 1
        return binary_search_with_recursion(array, value, left, new_right)

    if array[middle] < value:
        new_left = middle + 1
        return binary_search_with_recursion(array, value, new_left, right)

    return middle


def binary_search_with_cycle(array, value):
    left = 0
    right = len(array) - 1

    while True:
        if left > right:
            return -1

        middle = (left + right) // 2

        if array[middle] > value:
            right = middle - 1
            continue

        if array[middle] < value:
            left = middle + 1
            continue

        return middle


numbers_list = [1, 3, 5, 7, 8]
print(f'Список {numbers_list}')
number = int(input(f'Введите значение элемента: '))

print(f'Элемент {number} найден под индексом '
      f'{binary_search_with_recursion(numbers_list, number, 0, len(numbers_list) - 1)}')
print(f'Элемент {number} найден под индексом '
      f'{binary_search_with_cycle(numbers_list, number)}')
