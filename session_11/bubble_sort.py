def bubble_sort(values_list):
    for i in range(len(values_list) - 1):
        was_exchange = False

        for j in range(len(values_list) - 1 - i):
            if values_list[j] > values_list[j + 1]:
                values_list[j], values_list[j + 1] = values_list[j + 1], values_list[j]
                was_exchange = True

        if not was_exchange:
            return


list_to_sort = [5, 4, 5, 2, 1]
bubble_sort(list_to_sort)
print(f'Отсортированный список: {list_to_sort}')
