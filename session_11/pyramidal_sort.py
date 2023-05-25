def get_max_element_index_value(number_1, number_2):
    if number_1 > number_2:
        return 1

    return 2


def do_sifting(array, current_index, sorted_array_length=0):
    index_value = 0

    while 2 * current_index + 1 < len(array) - sorted_array_length:
        index_1 = 2 * current_index + 1
        index_2 = 2 * current_index + 2

        if 2 * current_index + 2 >= len(array) - sorted_array_length:
            if array[current_index] < array[index_1]:
                array[current_index], array[index_1] = array[index_1], array[current_index]

            return

        if array[current_index] < array[index_1] or array[current_index] < array[index_2]:
            index_value = get_max_element_index_value(array[index_1], array[index_2])
            array[current_index], array[2 * current_index + index_value] = \
                array[2 * current_index + index_value], array[current_index]

        current_index = 2 * current_index + index_value

        if current_index == 0:
            return


numbers_list = [1000000, -2562, 3, 6, 8, 7, 1, 12]

for i in range(len(numbers_list) // 2 - 1, -1, -1):
    do_sifting(numbers_list, i)

for i in range(len(numbers_list) - 1):
    numbers_list[0], numbers_list[len(numbers_list) - 1 - i] = numbers_list[len(numbers_list) - 1 - i], numbers_list[0]
    do_sifting(numbers_list, 0, i + 1)

print(numbers_list)
