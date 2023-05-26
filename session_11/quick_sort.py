def quick_sort(array, left, right):
    if right - left + 1 == 1:
        return

    if right - left + 1 == 2:
        if array[right] < array[left]:
            array[right], array[left] = array[left], array[right]

        return

    support_element = array[left]
    i = left
    j = right

    while i <= j:
        while array[i] < support_element:
            i += 1

        while array[j] > support_element:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if i < right:
        quick_sort(array, i, right)

    if j > left:
        quick_sort(array, left, j)

    return


numbers_list = [300, 5, 1, 24, 8, -5, 0]
quick_sort(numbers_list, 0, len(numbers_list) - 1)
print(f'Отсортированный список: {numbers_list}')
