def create_art(file_in, file_out='out.txt', cols=None, scale=0.5):
    im = convert_to_grayscale(file_in)
    width, height = im.size
    cols = cols if cols else width

    # calculate width and height of tile
    width_tile = width / cols
    height_tile = width_tile / scale

    rows = int(height / height_tile)

    with open(file_out, 'w') as f:
        for y in range(rows):
            for x in range(cols):
                x1, y1, x2, y2 = x * width_tile, y * height_tile, (x + 1) * width_tile, (y + 1) * height_tile
                cropped_im = im.crop((x1, y1, x2, y2))  # get image tile
                avg_val = get_average_of_tile(cropped_im)
                f.write(GS_SYMBOLS[avg_val * 69 // 255])  # get ascii symbol
            f.write('\n')
    
    return 'Done'

