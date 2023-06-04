def bubble_sort(numbers_list):
    for i in range(len(numbers_list) - 1):
        was_exchange = False

        for j in range(len(numbers_list) - 1 - i):
            if numbers_list[j] > numbers_list[j + 1]:
                numbers_list[j], numbers_list[j + 1] = numbers_list[j + 1], numbers_list[j]
                was_exchange = True

        if not was_exchange:
            return


values_list = [5, 4, 5, 2, 1]
bubble_sort(values_list)
print(f'Отсортированный список: {values_list}')
