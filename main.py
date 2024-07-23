from scripts.create_art import create_art
from logo import LOGO


def main():
    print(LOGO)

    input_file = input('Name of input image (if left blank program terminates): ').strip()
    if not input_file:
        print('No input file specified')
        return

    output_file = input('Name of output file to write ascii art to (default is out.txt): ').strip()
    cols = input('Width of ASCII art (default is width of image after conversion): ').strip()
    scale = input('Scale of your font (default is 0.5): ').strip()
    
    # set default values if not provided
    output_file = output_file if output_file else 'out.txt'
    cols = int(cols) if cols else None
    scale = float(scale) if scale else 0.5

    print(create_art(input_file, output_file, cols, scale))
    return


if __name__ == "__main__":
    main()