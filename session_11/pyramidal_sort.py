def sift(numbers_list, parent_index, list_length):
    while 2 * parent_index + 1 < list_length:
        child_1_index = 2 * parent_index + 1
        child_2_index = 2 * parent_index + 2

        if child_2_index >= list_length:
            if numbers_list[parent_index] < numbers_list[child_1_index]:
                numbers_list[parent_index], numbers_list[child_1_index] = \
                    numbers_list[child_1_index], numbers_list[parent_index]

            return

        max_child_index = 2 * parent_index + 1 if numbers_list[child_1_index] > numbers_list[child_2_index] \
            else 2 * parent_index + 2

        if numbers_list[parent_index] >= numbers_list[max_child_index]:
            return

        numbers_list[parent_index], numbers_list[max_child_index] = \
            numbers_list[max_child_index], numbers_list[parent_index]
        parent_index = max_child_index


def pyramidal_sort(numbers_list):
    for i in range(len(numbers_list) // 2 - 1, -1, -1):
        sift(numbers_list, i, len(numbers_list))

    for i in range(len(numbers_list) - 1, 0, -1):
        numbers_list[0], numbers_list[i] = numbers_list[i], numbers_list[0]
        sift(numbers_list, 0, i)


values_list = [100, -25, 3, 6, 8, 7, 1, -12]
pyramidal_sort(values_list)
print(f'Отсортированный список: {values_list}')
