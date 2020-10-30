# `ImageDraw` tests
#
# Limitation of `ImageDraw`: the shapes drawn don't seem to be antialiased.

import os

from PIL import Image, ImageDraw


# MARK: - Polygon
def test_draw_polygon_with_key_points():
    image: Image.Image = Image.new("L", (100, 100), 0)

    key_points = ((25, 25), (25, 75), (50, 100), (75, 75), (75, 25), (50, 0))

    draw: ImageDraw.ImageDraw = ImageDraw.Draw(image)
    draw.polygon(key_points, fill=255)

    image.save("out/4/polygon_key_points.png")


def test_draw_regular_polygon():
    image: Image.Image = Image.new("L", (120, 120), 0)

    center_point = (60, 60)
    radius = 50
    sides = 6
    rotation = 30    # Rotation is in degrees

    draw = ImageDraw.Draw(image)
    draw.regular_polygon((center_point, radius), sides, rotation=rotation, fill=128, outline=255)

    image.save("out/4/regular_polygon.png")


# MARK: - Circle
def test_draw_circle_and_ellipse():
    """
    Strangely, ellipses are drawn using bounding boxes.

    But this way, in order to rotate them, I'll need to draw to a separate image, rotate, and paste.
    Super annoying!
    """
    image: Image.Image = Image.new("RGB", (100, 100), (255, 255, 255))

    # 2 acceptable bounding box formats.
    bounding_box_1 = (0, 10, 50, 40)    # (x0, y0, x1, y1)
    bounding_box_2 = ((50, 50), (100, 100))    # ((x0, y0), (x1, y1))

    fill_color = (254, 193, 188)
    stroke_color = (254, 107, 123)
    stroke_width = 3

    draw = ImageDraw.Draw(image)
    draw.ellipse(bounding_box_1, fill=fill_color, outline=stroke_color, width=stroke_width)
    draw.ellipse(bounding_box_2, fill=fill_color, outline=stroke_color, width=stroke_width)

    image.save("out/4/circle_and_ellipse.png")


# MARK: - Main
if (__name__ == "__main__"):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(f"Working directory: {os.getcwd()}")

    # test_draw_polygon_with_key_points()
    # test_draw_regular_polygon()

    test_draw_circle_and_ellipse()
