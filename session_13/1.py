from PIL import Image


def f(pixels, x, y, matrix, width, height):
    red = 0
    green = 0
    blue = 0

    _x_start = x - len(matrix) // 2
    _x_end = x + len(matrix) // 2
    _y_start = y - len(matrix) // 2
    _y_end = y + len(matrix) // 2

    if x - len(matrix) // 2 < 0:
        _x_start = 0

    if x + len(matrix) // 2 > width:
        _x_end = width

    if y - len(matrix) // 2 < 0:
        _y_start = 0

    if y + len(matrix) // 2 > height:
        _y_end = height

    for i in range(_x_start, _x_end + 1):
        for j in range(_y_start, _y_end + 1):
            if i != x or j != y:
                current_pixel = pixels[i, j]
                red += current_pixel[0] * matrix[i % len(matrix)][j % len(matrix)]
                green += current_pixel[1] * matrix[i % len(matrix)][j % len(matrix)]
                blue += current_pixel[2] * matrix[i % len(matrix)][j % len(matrix)]

    return round(red), round(green), round(blue)


input_image = Image.open('image.jpg')
output_image = Image.open('out.jpg')
input_pixels = input_image.load()
output_pixels = output_image.load()

width, height = input_image.size
# output_pixels = [[0] * height for i in range(width)]

COEFFICIENT = 1 / 9
DIMENSION = 3
matrix = [[COEFFICIENT] * DIMENSION for i in range(DIMENSION)]

for x in range(1, width - 1):
    for y in range(1, height - 1):
        output_pixels[x, y] = f(input_pixels, x, y, matrix, width, height)

output_image.save("out.jpg")
