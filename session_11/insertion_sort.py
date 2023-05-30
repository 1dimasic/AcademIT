def insertion_sort_v_1(_list):
    for i in range(1, len(_list)):
        temp = _list[i]

        for j in range(i - 1, -2, -1):
            if temp >= _list[j] or j < 0:
                _list[j + 1] = temp
                break

            _list[j + 1] = _list[j]


def insertion_sort_v_2(_list):
    for i in range(1, len(_list)):
        temp = _list[i]
        j = i - 1

        while _list[j] >= temp and j >= 0:
            _list[j + 1] = _list[j]
            j -= 1

        _list[j + 1] = temp


numbers_list = [18, 5, 3, -10]
insertion_sort_v_1(numbers_list)
print(f'Отсортированный список: {numbers_list}')

numbers_list = [18, 5, 3, -10]
insertion_sort_v_2(numbers_list)
print(f'Отсортированный список: {numbers_list}')
