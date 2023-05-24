def reverse_list(array):
    for i in range(len(array) // 2):
        array[i], array[-i - 1] = array[-i - 1], array[i]

    return array


numbers_list = [4, 6, 8, 10, 7]
print(f'Список в обратном порядке: {reverse_list(numbers_list)}')
