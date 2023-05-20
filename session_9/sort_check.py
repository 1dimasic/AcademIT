# по возрастанию
def is_ascending_sorted():
    for index in range(len(number_list) - 1):
        if number_list[index] > number_list[index + 1]:
            return False

    return True


# по убыванию
def is_descending_sorted():
    for index in range(len(number_list) - 1):
        if number_list[index] < number_list[index + 1]:
            return False

    return True


number_list = [9, 8, 7, 6]
print(f'Список {number_list} отсортирован по возрастанию?..', is_ascending_sorted())
print(f'Список {number_list} отсортирован по убыванию?.....', is_descending_sorted())

number_list = [1, 2, 3, 4]
print(f'Список {number_list} отсортирован по возрастанию?..', is_ascending_sorted())
print(f'Список {number_list} отсортирован по убыванию?.....', is_descending_sorted())

number_list = [1, 4, 7, 4]
print(f'Список {number_list} отсортирован по возрастанию?..', is_ascending_sorted())
print(f'Список {number_list} отсортирован по убыванию?.....', is_descending_sorted())
