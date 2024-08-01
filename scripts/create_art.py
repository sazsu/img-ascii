from scripts.convert_to_gs import convert
from scripts.get_average_brightness import get_average


GS_SYMBOLS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "


def create_art(file_in, file_out, cols, scale):
    im = convert(file_in)
    width, height = im.size
    cols = cols if cols else width

    # calculate width and height of tile
    width_tile = width / cols
    height_tile = width_tile / scale

    rows = int(height / height_tile)

    with open(file_out, "w") as f:
        for y in range(rows):
            for x in range(cols):
                x1, y1, x2, y2 = (
                    x * width_tile,
                    y * height_tile,
                    (x + 1) * width_tile,
                    (y + 1) * height_tile,
                )
                cropped_im = im.crop((x1, y1, x2, y2))  # get image tile
                avg_val = get_average(cropped_im)
                f.write(GS_SYMBOLS[avg_val * 69 // 255])  # get ascii symbol
            f.write("\n")

    return f"ASCII art created in {file_out}"
