#!/usr/bin/env python3
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageOps
from PIL import ImageColor
import random
import argparse
import os

DEFAULT_DIR = "/usr/share/archur"

themes = {
    "solarized": {
        "text": (147, 161, 161),
        "logo": (147, 161, 161),
        "background": (0, 43, 54),
    },
    "black": {
        "text": (255, 255, 255),
        "logo": (255, 255, 255),
        "background": (0, 0, 0),
    },
    "standart": {
        "text": (77, 77, 77),
        "logo": (23, 147, 209),
        "background": (255, 255, 255),
    },
    "inverted": {
        "text": (255, 255, 255),
        "logo": (23, 147, 209),
        "background": (51, 51, 51),
    },
}

def get_random_text():
    with open(DEFAULT_DIR + '/text.txt') as f:
        lines = f.read().splitlines()
    return random.choice(lines) if lines else ""

def get_random_theme():
    return random.choice(list(themes.values()))

def text_draw(draw, text, pixel, ress, theme):
    text = text.split("\\n")
    W, H = ress
    base_height = (H / 100) * 70
    for i in text:
        font = ImageFont.truetype("DejaVuSansMono.ttf", pixel)
        bbox = draw.textbbox((0, base_height), i, font=font)  # Get the bounding box
        w = bbox[2] - bbox[0]  # Width = right - left
        draw.text(((W - w) / 2, base_height), i, theme["text"], font=font)
        base_height += (H / 100) * 8

def generate_img(output="", theme={}, text="", resolution=(1920, 1080), text_scale=1.0, logo_scale=1.0):
    img = Image.new("RGB", resolution, theme["background"])
    W, H = img.size

    logo = Image.open(DEFAULT_DIR + "/assets/logo.png")
    colorized_img = ImageOps.colorize(logo.convert("L"), theme["logo"], theme["background"])
    size = int((W / 100) * 17 * logo_scale)
    logo_newsize = colorized_img.resize((size, size), Image.LANCZOS)
    img.paste(logo_newsize, (int((W - size) / 2), int((H - size) / 2)))

    draw = ImageDraw.Draw(img)

    base_font_pixel = int((56 / 1920) * resolution[0] * text_scale)
    text_draw(draw, text, base_font_pixel, img.size, theme)

    img.save(output, quality=100)

def main():
    parser = argparse.ArgumentParser(description='Generate random Arch wallpapers')
    parser.add_argument('-o', '--output-dir', help='Output directory for images', required=True)
    parser.add_argument('-n', '--num-images', type=int, default=50, help='Number of images to generate', required=False)
    parser.add_argument('-t', '--theme', default="random",
                        help='The theme to use, else random. \'black\', \'solarized\', \'standart\' or \'inverted\'', required=False)
    parser.add_argument('--text', default="random", help='Text on the picture, or "random"', required=False)
    parser.add_argument('-r', '--resolution', default=(1920, 1080), help='Sets the resolution of the image. Example: 1920x1080', required=False)
    parser.add_argument('-ts', '--text-scale', default=(1.0), help='Sets scale for the text. Example: 1.75', required=False)
    parser.add_argument('-ls', '--logo-scale', default=(1.0), help='Sets scale for the logo. Example: 3.0', required=False)
    parser.add_argument('-fg', '--foreground-color', type=str, help='Color for the text and the logo.', required=False)
    parser.add_argument('-bg', '--background-color', type=str, help='Color for the background.', required=False)

    args = vars(parser.parse_args())

    output_dir = args["output_dir"]
    os.makedirs(output_dir, exist_ok=True)  # Create output directory if it does not exist

    for i in range(args["num_images"]):
        output = os.path.join(output_dir, f"wallpaper_{i + 1}.png")

        # Randomize the theme if "random" is specified
        if args["theme"] == "random":
            theme = get_random_theme()
        else:
            theme = themes[args["theme"]]

        # Use random text if specified
        text = get_random_text() if args["text"] == "random" else args["text"]

        # Generate image
        generate_img(output=output, theme=theme, text=text, resolution=tuple(map(int, args["resolution"].split('x'))),
                     text_scale=float(args["text_scale"]), logo_scale=float(args["logo_scale"]))

if __name__ == '__main__':
    main()
