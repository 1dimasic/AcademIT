def quick_sort(numbers_list, left, right):
    if right <= 0:
        return

    if right - left + 1 == 2:
        if numbers_list[right] < numbers_list[left]:
            numbers_list[right], numbers_list[left] = numbers_list[left], numbers_list[right]

        return

    support_element = numbers_list[left]
    i = left
    j = right

    while i <= j:
        while numbers_list[i] < support_element:
            i += 1

        while numbers_list[j] > support_element:
            j -= 1

        if i <= j:
            numbers_list[i], numbers_list[j] = numbers_list[j], numbers_list[i]
            i += 1
            j -= 1

    if i < right:
        quick_sort(numbers_list, i, right)

    if j > left:
        quick_sort(numbers_list, left, j)


values_list = [300]#, 5, 1, 24, 8, -5, 0]
quick_sort(values_list, 0, len(values_list) - 1)
print(f'Отсортированный список: {values_list}')
