def quick_sort(values_list, left, right):
    if right <= left:
        return

    if right - left + 1 == 2:
        if values_list[right] < values_list[left]:
            values_list[right], values_list[left] = values_list[left], values_list[right]

        return

    support_element = values_list[left]
    i = left
    j = right

    while i <= j:
        while values_list[i] < support_element:
            i += 1

        while values_list[j] > support_element:
            j -= 1

        if i <= j:
            values_list[i], values_list[j] = values_list[j], values_list[i]
            i += 1
            j -= 1

    if i < right:
        quick_sort(values_list, i, right)

    if j > left:
        quick_sort(values_list, left, j)


list_to_sort = [2, 8, 7, -5, 1]
quick_sort(list_to_sort, 0, len(list_to_sort) - 1)
print(f'Отсортированный список: {list_to_sort}')
