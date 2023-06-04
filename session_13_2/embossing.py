from PIL import Image
import convolution
import saturation

matrix = [[0, 1, 0], [-1, 0, 1], [0, -1, 0]]

input_image = Image.open('image_black_and_white.jpg')
input_width, input_height = input_image.size
input_pixels = input_image.load()

output_image = input_image.copy()
output_pixels = output_image.load()

temp_image = input_image.resize((input_width + len(matrix) // 2, input_height + len(matrix) // 2))
temp_pixels = temp_image.load()

for coordinate_x in range(input_width):
    for coordinate_y in range(input_height):
        output_pixels[coordinate_x, coordinate_y] = saturation.saturation(
            convolution.make_convolution(temp_pixels, matrix, coordinate_x, coordinate_y), 128)

output_image.resize((input_width, input_height))
output_image.save("output.jpg")
