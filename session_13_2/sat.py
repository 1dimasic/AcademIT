def sat(colors, value):
    result = [color + value for color in colors]

    for i in range(len(result)):
        if result[i] < 0:
            result[i] = 0

        if result[i] > 255:
            result[i] = 255

    return tuple(result)


def add(colors, value):
    result = [value + color for color in colors]

    return tuple(result)
