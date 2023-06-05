def g(matrix, i):
    return [row[:i] + row[i + 1:] for row in matrix[1:]]


def f(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    d = 0
    for i in range(len(matrix)):
        d += (-1) ** i * matrix[0][i] * f(g(matrix, i))
    return d


D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

