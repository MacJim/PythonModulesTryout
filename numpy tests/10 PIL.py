# PIL image expanding.

import os

import PIL.Image as Image
import PIL.ImageOps
import numpy as np


def test1():
    image: Image.Image = Image.open("abc.png")
    print(image.mode, image.size)

    array = np.array(image)

    recreated_image = Image.fromarray(array)
    print(recreated_image.mode, recreated_image.size)


def test2():
    image: Image.Image = Image.open("abc.png")
    print("Mode:", image.mode)

    array = np.array(image)
    print("Dtype:", array.dtype)
    print("Shape:", array.shape)    # 316, 316, 4

    # Pad 0.
    # padded_image = PIL.ImageOps.pad(image, (400, 400), color=(255, 255, 255))    # The `pad` function simply scales the original image. Not sure about its name origin.
    expanded_image = PIL.ImageOps.expand(image, border=100, fill=(255, 255, 255, 255))
    print("Expanded mode:", expanded_image.mode)
    expanded_image.save("abc2.png")


os.chdir(os.path.abspath(os.path.dirname(__file__)))
test1()
# test2()
