# Flipping an image.

import numpy as np
import PIL.Image as Image


# a: np.ndarray = np.arange(9)
# a.reshape(3, 3)    # Note that the reshape operation returns a copy and thus this operation does nothing useful.
# a = a.reshape(3, -1)
# print("Original:", a)
#
# a1 = np.rot90(a, k=1, axes=(0, 1))
# print("a1:", a1)
# a1 = np.rot90(a, k=1, axes=(1, 0))
# print("a1:", a1)


source_image = Image.open("../abc.png")
source_array = np.array(source_image)
print("Source np array shape:", source_array.shape)    # (316, 316, 4)

image1 = Image.fromarray(source_array)
# image1.show()


# MARK: - np.rot90
# axes: The array is rotated in the plane defined by the axes. Default: (0, 1)

# CCW 90
array_rot1 = np.rot90(source_array, k=1, axes=(0, 1))
image_rot1 = Image.fromarray(array_rot1)
# image_rot1.show()

# CW 90
array_rot2 = np.rot90(source_array, k=1, axes=(1, 0))
image_rot2 = Image.fromarray(array_rot2)
# image_rot2.show()

# CCW 270 (the same as CW 90)
array_rot3 = np.rot90(source_array, k=3, axes=(0, 1))
image_rot3 = Image.fromarray(array_rot3)
# image_rot3.show()

# 180
array_rot4 = np.rot90(source_array, k=2, axes=(0, 1))
image_rot4 = Image.fromarray(array_rot4)
# image_rot4.show()

# A flipped, reddish image. Do not do this.
array_rot5 = np.rot90(source_array, k=2, axes=(1, 2))
image_rot5 = Image.fromarray(array_rot5)
# image_rot5.show()


# MARK: - np.fliplr/flipud

# Flipped horizontally.
array_flip1 = np.fliplr(source_array)
image_flip1 = Image.fromarray(array_flip1)
# image_flip1.show()

# Flipped vertically.
array_flip2 = np.flipud(source_array)
image_flip2 = Image.fromarray(array_flip2)
# image_flip2.show()


# MARK: - (Useless) playground

# CW 90 -> flip horizontally.
array_play1 = np.fliplr(np.rot90(source_array, k=3))
image_play1 = Image.fromarray(array_play1)
image_play1.show()

array_play2 = np.rot90(np.fliplr(array_play1))    # Restores `array_play1` to normal.
image_play2 = Image.fromarray(array_play2)
image_play2.show()
