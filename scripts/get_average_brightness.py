def get_average(im):
    width, height = im.size
    values = []

    for x in range(width):
        for y in range(height):
            values.append(im.getpixel((x, y)))

    return sum(values) // len(values)

