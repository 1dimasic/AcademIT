import numpy as np

#
# def g(array, j):
#     l = array[1:, j:] + array[1:, :j + 1]
#     return l
#
#
# def f(array):
#     if len(array) == 2:
#         return array[0, 0] * array[1, 1] - array[0, 1] * array[1, 0]
#
#     d = 0
#     for i in range(len(l)):
#         d += (-1) ** i * array[0][i] * f(g(array, i))
#     return d


# l = np.array([[1, 2, 1], [2, 1, 2], [1, 1, 2]])
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(l)):
    print(l[1:][i:])
