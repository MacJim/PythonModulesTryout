# Crop an image.

import os

import PIL.Image as Image


def test_crop_1():
    """
    Crop from center and top left.
    """
    image = Image.open("../abc.png")
    width, height = image.size
    print(f"Original size: {width}, {height}")    # (316, 316)

    center_cropped_image: Image.Image = image.crop((width / 4, height / 4, width * 3 / 4, height * 3 / 4))
    print(f"Center cropped size: {center_cropped_image.size}")    # (158, 158)
    # center_cropped_image.save("out/abc_cropped_center.png")

    top_left_cropped_image: Image.Image = image.crop((0, 0, width / 2, height / 2))
    print(f"Top left cropped size: {top_left_cropped_image.size}")    # (158, 158)
    top_left_cropped_image.save("out/abc_cropped_top_left.png")


def test_crop_2():
    """
    Crop a single pixel.

    If `(x0 == x1)` and `(y0 == y1)`, the resulting image will have size (0, 0).
    Images with 0 width or 0 height cannot be saved correctly (throws an exception and leaves a corrupt file on disk).
    """
    image: Image.Image = Image.open("../abc.png")
    width, height = image.size

    pixel_cropped_image_1: Image.Image = image.crop((width / 2, height / 2, width / 2, height / 2))
    print(f"Pixel cropped image 1 size: {pixel_cropped_image_1.size}")    # (0, 0)
    # pixel_cropped_image_1.save("out/abc_cropped_pixel_1.png")    # Results in an exception and a corrupt file.

    pixel_cropped_image_2: Image.Image = image.crop((width / 2, height / 2, width / 2 + 1, height / 2))
    print(f"Pixel cropped image 2 size: {pixel_cropped_image_2.size}")    # (1, 0)
    # pixel_cropped_image_2.save("out/abc_cropped_pixel_2.png")    # Results in an exception and a corrupt file.

    pixel_cropped_image_3: Image.Image = image.crop((width / 2, height / 2, width / 2 + 1, height / 2 + 1))
    print(f"Pixel cropped image 3 size: {pixel_cropped_image_3.size}")    # (1, 1)
    pixel_cropped_image_3.save("out/abc_cropped_pixel_3.png")


if (__name__ == "__main__"):
    os.chdir(os.path.dirname(__file__))
    # print(f"Working directory: {os.getcwd()}")
    # test_crop_1()
    test_crop_2()
