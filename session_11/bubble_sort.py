def bubble_sort(array):
    for j in range(len(array) - 1):
        exchanges_count = 0

        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                exchanges_count = +1

            if exchanges_count == 0:
                return


numbers_list = [8, 5, 3, 2, 1, -1]
bubble_sort(numbers_list)
print(f'Отсортированный список: {numbers_list}')
