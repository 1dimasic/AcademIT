def insertion_sort_v_1(numbers_list):
    for i in range(1, len(numbers_list)):
        temp = numbers_list[i]

        for j in range(i - 1, -2, -1):
            if temp >= numbers_list[j] or j < 0:
                numbers_list[j + 1] = temp
                break

            numbers_list[j + 1] = numbers_list[j]


def insertion_sort_v_2(numbers_list):
    for i in range(1, len(numbers_list)):
        temp = numbers_list[i]
        j = i - 1

        while numbers_list[j] >= temp and j >= 0:
            numbers_list[j + 1] = numbers_list[j]
            j -= 1

        numbers_list[j + 1] = temp


values_list = [18, 5, 3, -10]
insertion_sort_v_1(values_list)
print(f'Отсортированный список: {values_list}')

values_list = [18, 5, 3, -10]
insertion_sort_v_2(values_list)
print(f'Отсортированный список: {values_list}')
