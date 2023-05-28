def reverse_list(values_list):
    for i in range(len(values_list) // 2):
        values_list[i], values_list[-i - 1] = values_list[-i - 1], values_list[i]

    return values_list


numbers_list = [4, 6, 8, 10, 7]
print(f'Список в обратном порядке: {reverse_list(numbers_list)}')
