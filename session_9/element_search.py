def get_element_index_v_1(values_list, element):
    for i in range(len(values_list)):
        if values_list[i] == element:
            return i

    return -1


def get_element_index_v_2(values_list, element):
    for i, value in enumerate(values_list):
        if value == element:
            return i

    return -1


numbers_list = [-5, 6, 2, 89, 9]
functions = (get_element_index_v_1, get_element_index_v_2)

print("Список ", numbers_list)

for function in functions:
    entered_number = int(input('Введите число: '))
    print(f'Индекс элемента списка = {function(numbers_list, entered_number)}')
