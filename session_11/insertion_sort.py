def insertion_sort_v_1(values_list):
    for i in range(1, len(values_list)):
        temp = values_list[i]

        for j in range(i - 1, -2, -1):
            if temp >= values_list[j] or j < 0:
                values_list[j + 1] = temp
                break

            values_list[j + 1] = values_list[j]


def insertion_sort_v_2(values_list):
    for i in range(1, len(values_list)):
        temp = values_list[i]
        j = i - 1

        while values_list[j] >= temp and j >= 0:
            values_list[j + 1] = values_list[j]
            j -= 1

        values_list[j + 1] = temp


list_to_sort = [18, 5, 3, -10]
insertion_sort_v_1(list_to_sort)
print(f'Отсортированный список: {list_to_sort}')

list_to_sort = [18, 5, 3, -10]
insertion_sort_v_2(list_to_sort)
print(f'Отсортированный список: {list_to_sort}')
