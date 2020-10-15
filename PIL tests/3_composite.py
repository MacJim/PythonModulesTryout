# Composite 2 images.
# Source: https://note.nkmk.me/en/python-pillow-composite/
#
# Composite equivalence:
# - 1 bit mask: `result = mask * image1 + (1 - mask) * image2`
# - 8 bit mask: `result = mask / 255 * image1 + (1 - mask / 255 ) * image2`

import os

from PIL import Image, ImageDraw, ImageFilter


def test_composite_uniformly():
    """
    Blend 2 images uniformly.
    """
    image1: Image.Image = Image.open("../sfu1.png")
    image2: Image.Image = Image.open("../sfu2.png")
    print(f"Image 1 size: {image1.size}")    # (1200, 675)
    print(f"Image 2 size: {image2.size}")    # (1200, 675)

    blend_ratio = 192    # /255
    mask = Image.new("L", image1.size, blend_ratio)

    composite_image = Image.composite(image1, image2, mask)
    composite_image.save("out/composite_uniform.png")


def test_composite_horizontal_gradient():
    image1: Image.Image = Image.open("../sfu1.png")
    image2: Image.Image = Image.open("../sfu2.png")

    mask: Image.Image = Image.open("../horizontal_gradient.png")
    # print(mask.mode)
    mask = mask.convert("L").resize(image1.size)

    composite_image = Image.composite(image1, image2, mask)
    composite_image.save("out/composite_horizontal.png")


def test_composite_draw_mask():
    """
    Use `ImageDraw` to draw a mask.
    """
    image1: Image.Image = Image.open("../sfu1.png")
    image2: Image.Image = Image.open("../sfu2.png")

    mask: Image.Image = Image.new("L", image1.size, 0)    # Black mask
    draw: ImageDraw.Draw = ImageDraw.Draw(mask)    # A little alias effect here.
    draw.ellipse((mask.size[0] / 4, mask.size[1] / 2 - mask.size[0] / 4, mask.size[0] * 3 / 4, mask.size[1] / 2 + mask.size[0] / 4), fill = 255)
    mask.save("out/circle_mask.png")

    composite_image = Image.composite(image1, image2, mask)
    composite_image.save("out/composite_circle.png")

    blurred_mask = mask.filter(ImageFilter.GaussianBlur(6))
    blurred_mask.save("out/circle_mask_blurred.png")

    blurred_composite_image = Image.composite(image1, image2, blurred_mask)
    blurred_composite_image.save("out/composite_circle_blurred.png")


# MARK: - Main
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(f"Working directory: {os.getcwd()}")

# test_composite_uniformly()
# test_composite_horizontal_gradient()
test_composite_draw_mask()
