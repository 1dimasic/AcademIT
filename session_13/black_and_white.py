from PIL import Image

image = Image.open("image.jpg")
pixels = image.load()
width, height = image.size

for x in range(width):
    for y in range(height):
        pixel = pixels[x, y]
        rgb_result = round(0.3 * pixel[0] + 0.59 * pixel[1] + 0.11 * pixel[2])
        pixels[x, y] = (rgb_result, rgb_result, rgb_result)

image.save("image_black_and_white.jpg")
