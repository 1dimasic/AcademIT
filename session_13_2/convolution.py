def make_convolution(pixels, matrix, x, y):
    red = 0
    green = 0
    blue = 0
    size = len(matrix)

    for i, j in zip(range(x - size // 2, x + size // 2 + 1), range(size)):
        for k, n in zip(range(y - size // 2, y + size // 2 + 1), range(size)):
            pixel = pixels[i, k]
            red += pixel[0] * matrix[j][n]
            green += pixel[1] * matrix[j][n]
            blue += pixel[2] * matrix[j][n]

    return round(red), round(green), round(blue)
