def get_max_element_index_value(number_1, number_2):
    if number_1 > number_2:
        return 1

    return 2


def gf(array, i, j=0):
    max_element_index_value = 0
    while 2 * i + 1 < len(array) - j:
        if 2 * i + 2 >= len(array) - j:
            if l[i] < l[2 * i + 1]:
                l[i], l[2 * i + 1] = l[2 * i + 1], l[i]
            break

        if l[i] < l[2 * i + 1] or l[i] < l[2 * i + 1]:
            max_element_index_value = get_max_element_index_value(l[2 * i + 1], l[2 * i + 2])
            l[i], l[2 * i + max_element_index_value] = l[2 * i + max_element_index_value], l[i]

        i = 2 * i + max_element_index_value


def do_sifting(array, j):
    i = 0
    gf(array, i, j)


def g(array):
    for j in range(len(l) // 2 - 1, -1, -1):
        gf(array, j)


l = [1, 4, 5, 3, 4, 9, 1, 10]

g(l)
for i in range(len(l)):
    l[0], l[len(l) - 1 - i] = l[len(l) - 1 - i], l[0]
    do_sifting(l, i + 1)
print(l)
