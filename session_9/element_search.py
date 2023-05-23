def get_element_index_v_1(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i

    return -1


def get_element_index_v_2(array, element):
    for i, number in enumerate(array):
        if number == element:
            return i

    return -1


numbers = [-5, 6, 2, 89, 9]
functions = (get_element_index_v_1, get_element_index_v_2)

print("Список ", numbers)

for j in range(2):
    entered_number = int(input('Введите число: '))
    print(f'Индекс элемента списка = {functions[j](numbers, entered_number)}')
