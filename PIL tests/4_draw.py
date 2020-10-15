# `ImageDraw` tests

import os

from PIL import Image, ImageDraw


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


# MARK: - Main
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(f"Working directory: {os.getcwd()}")

# test_draw_polygon_with_key_points()
test_draw_regular_polygon()
