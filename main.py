from PIL import ImageOps, Image

GS_SYMBOLS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "


def convert_to_grayscale(file_in):
    im = Image.open(file_in)

    gray_im = ImageOps.grayscale(im)
    gray_im.thumbnail((400, 400))  # resize image
    
    return gray_im


def get_average_of_tile(im):
    im
    width, height = im.size
    values = []

    for x in range(width):
        for y in range(height):
            values.append(im.getpixel((x, y)))

    return sum(values) // len(values)


def create_ascii_art(file_in, file_out='out.txt', cols=None, scale=0.5):
    im = convert_to_grayscale(file_in)
    width, height = im.size
    cols = cols if cols else width

    # calculate width and height of tile
    width_tile = width / cols
    height_tile = width_tile / scale

    rows = int(height / height_tile)

    res = []  # list to store ascii art symbols
    for y in range(rows):
        for x in range(cols):
            x1, y1, x2, y2 = x * width_tile, y * height_tile, (x + 1) * width_tile, (y + 1) * height_tile
            cropped_im = im.crop((x1, y1, x2, y2))  # get image tile
            avg_val = get_average_of_tile(cropped_im)
            res.append(GS_SYMBOLS[avg_val * 69 // 255])  # get ascii symbol
        res.append('\n')
    
    return ''.join(res)
