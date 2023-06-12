from PIL import Image


def saturate(colors):
    rgb_result = list(colors)

    for i in range(len(rgb_result)):
        if rgb_result[i] <= 0:
            rgb_result[i] = 0
        elif rgb_result[i] >= 255:
            rgb_result[i] = 255
        else:
            rgb_result[i] = round(rgb_result[i])

    return tuple(rgb_result)


DIMENSION = 8
matrix = [[1 / DIMENSION ** 2] * DIMENSION for i in range(DIMENSION)]
size = len(matrix)
size_half = size // 2

input_image = Image.open('image.jpg')
width, height = input_image.size
input_pixels = input_image.load()

output_image = input_image.copy()
output_pixels = output_image.load()

for x in range(size_half, width - size_half):
    for y in range(size_half, height - size_half):
        red = 0
        green = 0
        blue = 0

        for i in range(size):
            for j in range(size):
                pixel = input_pixels[x - size_half + i, y - size_half + j]
                red += pixel[0] * matrix[i][j]
                green += pixel[1] * matrix[i][j]
                blue += pixel[2] * matrix[i][j]

        output_pixels[x, y] = saturate((red, green, blue))

output_image.crop((size_half, size_half, width - size_half, height - size_half)).save('output_image.jpg')
