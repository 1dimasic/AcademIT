def get_min_value_index(array, start_index):
    min_value = array[start_index]
    min_value_index = start_index

    for i in range(start_index, len(array)):
        if array[i] < min_value:
            min_value = array[i]
            min_value_index = i

    return min_value_index


numbers_list = [8, 7, 6, 5]

for j in range(len(numbers_list) - 1):
    index = get_min_value_index(numbers_list, j)
    numbers_list[j], numbers_list[index] = numbers_list[index], numbers_list[j]

print(f'Список после сортировки выбором: {numbers_list}')
