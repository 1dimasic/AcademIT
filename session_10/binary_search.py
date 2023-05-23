def binary_search_v_1(array, value, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2

    if array[middle] > value:
        right = middle - 1
        return binary_search_v_1(array, value, left, right)

    if array[middle] < value:
        left = middle + 1
        return binary_search_v_1(array, value, left, right)

    return middle


def binary_search_v_2(array, value):
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

print(f'Элемент {number} найден под индексом {binary_search_v_1(numbers_list, number, 0, len(numbers_list) - 1)}')
print(f'Элемент {number} найден под индексом {binary_search_v_2(numbers_list, number)}')
