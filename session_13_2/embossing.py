from PIL import Image


def satiate(colors, brightness):
    rgb_result = [color + brightness for color in colors]

    for i in range(len(rgb_result)):
        if rgb_result[i] < 0:
            rgb_result[i] = 0

        if rgb_result[i] > 255:
            rgb_result[i] = 255

    return tuple(rgb_result)


matrix = [[0, 1, 0], [-1, 0, 1], [0, -1, 0]]
BRIGHTNESS = 128
size = len(matrix)
size_half = size // 2

input_image = Image.open('image_black_and_white.jpg')
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

        output_pixels[x, y] = satiate((round(red), round(green), round(blue)), BRIGHTNESS)

output_image.crop((size_half, size_half, width - size_half, height - size_half)).save('output.jpg')
