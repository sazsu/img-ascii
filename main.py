from PIL import ImageOps, Image


def convert_to_grayscale(img):
    im = Image.open(img)

    gray_im = ImageOps.grayscale(im)
    gray_im.save('output.png', 'PNG')
