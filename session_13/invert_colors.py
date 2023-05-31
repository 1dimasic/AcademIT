from PIL import Image

# Загружаем картинку из файла
image = Image.open("image.jpg")

# Получаем двумерный массив пикселей
pixels = image.load()

# Заводим константу для максимального значения компонент цвета
MAX_RGB = 255

# Получаем размеры картинки
width, height = image.size

# Проходим по всем пикселям картинки
for x in range(width):
    for y in range(height):
        """
        Получаем пиксель с координатами x, y
        Он является tuple, в котором по порядку идут красная (индекс 0), зеленая (индекс 1), 
        синяя (индекс 2) компоненты
        """
        pixel = pixels[x, y]

        # вычисляем и присваиваем новое значение
        pixels[x, y] = (MAX_RGB - pixel[0], MAX_RGB - pixel[1], MAX_RGB - pixel[2])

# Сохраняем картинку в файл
image.save("out.png")
