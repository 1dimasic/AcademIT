from PIL import Image


def blur(pixels, matrix, x, y):
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


COEFFICIENT = 1 / 25
DIMENSION = 5
blur_matrix = [[COEFFICIENT] * DIMENSION for i in range(DIMENSION)]

input_image = Image.open('image.jpg')
input_width, input_height = input_image.size

output_image = input_image.copy()
output_pixels = output_image.load()

temp_image = input_image.resize((input_width + DIMENSION // 2, input_height + DIMENSION // 2))
temp_pixels = temp_image.load()

for coordinate_x in range(input_width):
    for coordinate_y in range(input_height):
        output_pixels[coordinate_x, coordinate_y] = blur(temp_pixels, blur_matrix, coordinate_x, coordinate_y)

output_image.resize((input_width, input_height))
output_image.save("output_image_5x5.png")
