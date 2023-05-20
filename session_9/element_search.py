def get_element_index_v_1(element):
    for i in range(len(numbers)):
        if numbers[i] == element:
            return i

    return -1


def get_element_index_v_2(element):
    for i, number in enumerate(numbers):
        if number == element:
            return i

    return -1


numbers = [-5, 6, 2, 89, 9]
numbers_func = (get_element_index_v_1, get_element_index_v_2)

print("Список ", numbers)

for j in range(2):
    entered_number = int(input('Введите число: '))
    print(f'Индекс элемента списка = {numbers_func[j](entered_number)}')
