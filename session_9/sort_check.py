# по возрастанию
def is_ascending_sorted(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False

    return True


# по убыванию
def is_descending_sorted(array):
    for i in range(len(array) - 1):
        if array[i] < array[i + 1]:
            return False

    return True


numbers_list = [9, 8, 7, 6]
print(f'Список {numbers_list} отсортирован по возрастанию?..', is_ascending_sorted(numbers_list))
print(f'Список {numbers_list} отсортирован по убыванию?.....', is_descending_sorted(numbers_list))

numbers_list = [1, 2, 3, 4]
print(f'Список {numbers_list} отсортирован по возрастанию?..', is_ascending_sorted(numbers_list))
print(f'Список {numbers_list} отсортирован по убыванию?.....', is_descending_sorted(numbers_list))

numbers_list = [1, 4, 7, 4]
print(f'Список {numbers_list} отсортирован по возрастанию?..', is_ascending_sorted(numbers_list))
print(f'Список {numbers_list} отсортирован по убыванию?.....', is_descending_sorted(numbers_list))
