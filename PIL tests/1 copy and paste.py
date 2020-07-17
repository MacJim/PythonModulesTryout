import os

import PIL.Image as Image


def test1():
    """
    Paste an image into a larger canvas.
    """
    original_image: Image.Image = Image.open("../abc.png")
    # print("Original size:", original_image.size)    # (316, 316)
    # print("Original mode:", original_image.mode)    # RGBA

    top_left_image: Image.Image = Image.new(original_image.mode, (original_image.size[0] * 2, original_image.size[1] * 2))
    # print("New size:", top_left_image.size)    # (632, 632)
    # print("New mode:", top_left_image.mode)    # RGBA
    # The box argument is either a 2-tuple giving the upper left corner, a 4-tuple defining the left, upper, right, and lower pixel coordinate, or None (same as (0, 0)).
    top_left_image.paste(original_image, original_image.getbbox())
    top_left_image.save("out/abc_top_left.png")

    center_image: Image.Image = Image.new(original_image.mode, (original_image.size[0] * 2, original_image.size[1] * 2))
    center_x0 = (center_image.size[0] - original_image.size[0]) // 2    # Remember to use integer division.
    center_y0 = (center_image.size[1] - original_image.size[1]) // 2
    center_image.paste(original_image, (center_x0, center_y0))
    center_image.save("out/abc_center.png")


def test2():
    """
    Paste an image into a smaller canvas.
    """
    original_image: Image.Image = Image.open("../abc.png")

    cropped_image_1 = Image.new(original_image.mode, (original_image.size[0] // 2, original_image.size[1] // 2))
    cropped_image_1_x0 = (cropped_image_1.size[0] - original_image.size[0]) // 2
    cropped_image_1_y0 = (cropped_image_1.size[1] - original_image.size[1]) // 2
    cropped_image_1.paste(original_image, (cropped_image_1_x0, cropped_image_1_y0))
    cropped_image_1.save(("out/abc_crop_1.png"))

    cropped_image_2 = Image.new(original_image.mode, (original_image.size[0] // 2, original_image.size[1] * 2), (255, 255, 255, 255))
    cropped_image_2_x0 = (cropped_image_2.size[0] - original_image.size[0]) // 2
    cropped_image_2_y0 = (cropped_image_2.size[1] - original_image.size[1]) // 2
    cropped_image_2.paste(original_image, (cropped_image_2_x0, cropped_image_2_y0))
    cropped_image_2.save(("out/abc_crop_2.png"))


# MARK: - Main
os.chdir(os.path.abspath(os.path.dirname(__file__)))
# test1()
test2()
