from PIL import Image, ImageOps


def convert(file_in):
    im = Image.open(file_in)

    gray_im = ImageOps.grayscale(im)
    gray_im.thumbnail((400, 400))  # resize image
    
    return gray_im

