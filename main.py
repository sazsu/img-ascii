from PIL import ImageOps, Image


def convert_to_grayscale(img):
    im = Image.open(img)

    gray_im = ImageOps.grayscale(im)
    gray_im.thumbnail((400, 400))  # resize image
    
    return gray_im

def get_average_of_tile(img):
    img = Image.open(img)
    width, height = img.size
    values = []

    for x in range(width):
        for y in range(height):
            values.append(img.getpixel((x, y)))

    return sum(values) // len(values)
