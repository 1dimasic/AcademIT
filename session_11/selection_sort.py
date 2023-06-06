def selection_sort(values_list):
    for i in range(len(values_list) - 1):
        min_number_index = i

        for j in range(i + 1, len(values_list)):
            if values_list[j] < values_list[min_number_index]:
                min_number_index = j

        values_list[i], values_list[min_number_index] = values_list[min_number_index], values_list[i]


list_to_sort = [8, -3, 2, 6, 10, 0]
selection_sort(list_to_sort)
print(f'Отсортированный список: {list_to_sort}')
