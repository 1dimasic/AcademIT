from PIL import Image


def water_colorize(pixels, x, y):
    red = []
    green = []
    blue = []

    for i in range(x - 5, x + 5 + 1):
        for j in range(y - 5, y + 5 + 1):
            pixel = pixels[i, j]
            red.append(pixel[0])
            green.append(pixel[1])
            blue.append(pixel[2])

    red.sort()
    green.sort()
    blue.sort()

    return red[12], green[12], blue[12]


input_image = Image.open('image.jpg')
input_width, input_height = input_image.size
input_pixels = input_image.load()

output_image = input_image.copy()
output_pixels = output_image.load()

temp_image = input_image.resize((input_width + 5, input_height + 5))
temp_pixels = temp_image.load()

for coordinate_x in range(input_width):
    for coordinate_y in range(input_height):
        output_pixels[coordinate_x, coordinate_y] = water_colorize(temp_pixels, coordinate_x, coordinate_y)

output_image.resize((input_width, input_height))
output_image.save("output.jpg")
