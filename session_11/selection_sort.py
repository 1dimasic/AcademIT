def get_min_value_index(_list, start_index):
    min_value_index = start_index

    for i in range(start_index + 1, len(_list)):
        if _list[i] < _list[min_value_index]:
            min_value_index = i

    return min_value_index


def selection_sort(_list):
    for i in range(len(_list) - 1):
        min_value_index = get_min_value_index(_list, i)
        _list[i], _list[min_value_index] = _list[min_value_index], _list[i]


numbers_list = [8, -3, 2, 6, 10, 0]
selection_sort(numbers_list)
print(f'Отсортированный список: {numbers_list}')
