def bubble_sort(_list):
    for i in range(len(_list) - 1):
        was_exchange = False

        for j in range(len(_list) - 1 - i):
            if _list[j] > _list[j + 1]:
                _list[j], _list[j + 1] = _list[j + 1], _list[j]
                was_exchange = True

        if not was_exchange:
            return


numbers_list = [5, 4, 5, 2, 1]
bubble_sort(numbers_list)
print(f'Отсортированный список: {numbers_list}')
