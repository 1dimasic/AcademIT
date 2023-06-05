from PIL import Image


def satiate(colors):
    rgb_result = [color for color in colors]

    for i in range(len(rgb_result)):
        if rgb_result[i] < 0:
            rgb_result[i] = 0

        if rgb_result[i] > 255:
            rgb_result[i] = 255

    return tuple(rgb_result)


size = 5
size_half = size // 2
result = size ** 2 // 2

input_image = Image.open('image.jpg')
width, height = input_image.size
pixels = input_image.load()

output_image_1 = input_image.copy()
output_pixels_1 = output_image_1.load()

for x in range(size_half, width - size_half):
    for y in range(size_half, height - size_half):
        red = []
        green = []
        blue = []

        for i in range(size):
            for j in range(size):
                pixel = pixels[x - size_half + i, y - size_half + j]
                red.append(pixel[0])
                green.append(pixel[1])
                blue.append(pixel[2])

        red.sort()
        green.sort()
        blue.sort()
        output_pixels_1[x, y] = red[result], green[result], blue[result]

output_image_2 = output_image_1.copy()
output_pixels_2 = output_image_2.load()

matrix = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
size = len(matrix)
size_half = size // 2

for x in range(size_half, width - size_half):
    for y in range(size_half, height - size_half):
        red = 0
        green = 0
        blue = 0

        for i in range(size):
            for j in range(size):
                pixel = output_pixels_1[x - size_half + i, y - size_half + j]
                red += pixel[0] * matrix[i][j]
                green += pixel[1] * matrix[i][j]
                blue += pixel[2] * matrix[i][j]

        output_pixels_2[x, y] = satiate((round(red), round(green), round(blue)))

output_image_2.crop((size_half, size_half, width - size_half, height - size_half)).save('output_image.jpg')
