def get_matrix_minor(matrix, i):
    return [column[:i] + column[i + 1:] for column in matrix[1:]]


def get_matrix_determinant(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant = 0

    for i in range(len(matrix)):
        determinant += (-1) ** i * matrix[0][i] * get_matrix_determinant(get_matrix_minor(matrix, i))

    return determinant


matrix_for_calculation = [[1, 2, 3], [4, 5, 6], [7, 8, 90]]
print(f'Определитель матрицы = {get_matrix_determinant(matrix_for_calculation)}')
