def insertion_sort_v_1(array):
    for i in range(1, len(array)):
        temp = array[i]

        for j in range(i - 1, -2, -1):
            if temp >= array[j] or j < 0:
                array[j + 1] = temp
                break

            array[j + 1] = array[j]


def insertion_sort_v_2(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1

        while array[j] >= temp and j >= 0:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = temp


numbers_list = [18, 5, 3, -10]
insertion_sort_v_1(numbers_list)
print(f'Отсортированный список: {numbers_list}')

numbers_list = [18, 5, 3, -10]
insertion_sort_v_2(numbers_list)
print(f'Отсортированный список: {numbers_list}')
