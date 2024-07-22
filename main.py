from PIL import ImageOps, Image


def convert_to_grayscale(img):
    im = Image.open(img)

    gray_im = ImageOps.grayscale(im)
    print(gray_im.getpixel((0, 0)))
    return gray_im


# GRAYSCALE =  '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}'
GRAYSCALE = '`^\”,:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'


def create_ascii(g_im):

    width, height = g_im.size
    pixels = g_im.load()
    ans = []

    for y in range(0, height, 2):
        for x in range(0, width - 1, 2):
            pix1 = pixels[x, y] // 3
            pix2 = pixels[x + 1, y] // 3
            pix3 = pixels[x, y + 1] // 3
            pix4 = pixels[x + 1, y + 1] // 3
            res = (pix1 + pix2 + pix3 + pix4) // 4
            ascii_index = int((len(GRAYSCALE) - 1) * (res / 255))
            ans.append(GRAYSCALE[ascii_index])
        ans.append('\n')
    return ''.join(ans)       
