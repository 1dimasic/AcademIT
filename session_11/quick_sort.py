def do_sorting(array, left, right):
    if len(array[left:right + 1]) == 1:
        pass
    elif len(array[left:right + 1]) == 2:
        if array[1] < array[0]:
            array[1], array[0] = array[0], array[1]

    else:
        support_element = (numbers_list[left] + numbers_list[right]) // 2
        i = left
        j = right

        while i <= j:
            while array[i] < support_element:
                i += 1

            while array[j] > support_element:
                j -= 1

            if i <= j:
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1

        if i < right:
            return do_sorting(array, i, right)

        if j > left:
            return do_sorting(array, left, j)

        return


numbers_list = [3, 5, 1, 2]
do_sorting(numbers_list, 0, len(numbers_list) - 1)
print(numbers_list)
