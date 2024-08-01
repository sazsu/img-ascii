from scripts.create_art import create_art
import argparse


def main(file_in, file_out, cols, scale):
    print(create_art(file_in, file_out, cols, scale))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert image to ASCII art.")
    parser.add_argument(
        "-i", "--input", type=str, required=True, help="name of input image"
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="out.txt",
        required=False,
        help="name of output file (default: out.txt)",
    )
    parser.add_argument(
        "-c",
        "--cols",
        type=int,
        default=None,
        required=False,
        help="integer width of desired art (default: width of input image)",
    )
    parser.add_argument(
        "-s",
        "--scale",
        type=float,
        default=0.5,
        required=False,
        help="float scale of your font (default: 0.5)",
    )

    args = parser.parse_args()
    file_in = args.input
    file_out = args.output
    cols = args.cols
    scale = args.scale

    main(file_in, file_out, cols, scale)
