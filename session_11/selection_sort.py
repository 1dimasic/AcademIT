def selection_sort(numbers_list):
    for i in range(len(numbers_list) - 1):
        min_number_index = i

        for j in range(i + 1, len(numbers_list)):
            if numbers_list[j] < numbers_list[min_number_index]:
                min_number_index = j

        numbers_list[i], numbers_list[min_number_index] = numbers_list[min_number_index], numbers_list[i]


values_list = [8, -3, 2, 6, 10, 0]
selection_sort(values_list)
print(f'Отсортированный список: {values_list}')
