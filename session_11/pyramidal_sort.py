def sift(values_list, parent_index, list_length):
    while 2 * parent_index + 1 < list_length:
        child_1_index = 2 * parent_index + 1
        child_2_index = 2 * parent_index + 2

        if child_2_index >= list_length:
            if values_list[parent_index] < values_list[child_1_index]:
                values_list[parent_index], values_list[child_1_index] = \
                    values_list[child_1_index], values_list[parent_index]

            return

        max_child_index = 2 * parent_index + 1 if values_list[child_1_index] > values_list[child_2_index] \
            else 2 * parent_index + 2

        if values_list[parent_index] >= values_list[max_child_index]:
            return

        values_list[parent_index], values_list[max_child_index] = \
            values_list[max_child_index], values_list[parent_index]
        parent_index = max_child_index


def pyramidal_sort(values_list):
    for i in range(len(values_list) // 2 - 1, -1, -1):
        sift(values_list, i, len(values_list))

    for i in range(len(values_list) - 1, 0, -1):
        values_list[0], values_list[i] = values_list[i], values_list[0]
        sift(values_list, 0, i)


list_to_sort = [100, -25, 3, 6, 8, 7, 1, -12]
pyramidal_sort(list_to_sort)
print(f'Отсортированный список: {list_to_sort}')
