def sift(_list, parent_index, list_length):
    while 2 * parent_index + 1 < list_length:
        child_1_index = 2 * parent_index + 1
        child_2_index = 2 * parent_index + 2

        if child_2_index >= list_length:
            if _list[parent_index] < _list[child_1_index]:
                _list[parent_index], _list[child_1_index] = _list[child_1_index], _list[parent_index]

            return

        max_child_index = 1 if _list[child_1_index] > _list[child_2_index] else 2

        if _list[parent_index] >= _list[2 * parent_index + max_child_index]:
            return

        _list[parent_index], _list[2 * parent_index + max_child_index] = \
            _list[2 * parent_index + max_child_index], _list[parent_index]
        parent_index = 2 * parent_index + max_child_index

        if parent_index == 0:
            return


def pyramidal_sort(_list):
    for i in range(len(_list) // 2 - 1, -1, -1):
        sift(_list, i, len(_list))

    for i in range(len(_list) - 1, -1, -1):
        _list[0], _list[i] = _list[i], _list[0]
        sift(_list, 0, i)


numbers_list = [100, -25, 3, 6, 8, 7, 1, 12]
pyramidal_sort(numbers_list)
print(f'Отсортированный список: {numbers_list}')
