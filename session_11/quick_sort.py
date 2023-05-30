def quick_sort(_list, left, right):
    if not _list:
        return

    if right - left + 1 == 1:
        return

    if right - left + 1 == 2:
        if _list[right] < _list[left]:
            _list[right], _list[left] = _list[left], _list[right]

        return

    support_element = _list[left]
    i = left
    j = right

    while i <= j:
        while _list[i] < support_element:
            i += 1

        while _list[j] > support_element:
            j -= 1

        if i <= j:
            _list[i], _list[j] = _list[j], _list[i]
            i += 1
            j -= 1

    if i < right:
        quick_sort(_list, i, right)

    if j > left:
        quick_sort(_list, left, j)


numbers_list = [300, 5, 1, 24, 8, -5, 0]
quick_sort(numbers_list, 0, len(numbers_list) - 1)
print(f'Отсортированный список: {numbers_list}')
