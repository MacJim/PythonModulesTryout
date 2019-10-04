import sys

import numpy as np


# MARK: 1. Basics
# # arange(n): [0:n]
# # reshape(row count, column count) -> similar to Matlab.
# a = np.arange(15).reshape(3, 5)    # 5 * 3 matrix.
# # <class 'numpy.ndarray'>
# aType = type(a)
#
# # shape: row count * column count (3 * 5)
# unusedShape = a.shape
#
# # ndim: number of axes (dimensions) (2)
# unusedDimensions = a.ndim
#
# # dtype: type of elements ("int64", seems like "numpy.int64")
# unusedType = a.dtype.name
#
# # itemsize: each element's size in bytes (8)
# unusedItemSize = a.itemsize
#
# # size: total number of elements (15)
# unusedSize = a.size


# MARK: 2. Basics
# b = np.array([6, 7, 8])
#
# # <class 'numpy.ndarray'>
# arrayType = type(b)
# # int64
# elementType = b.dtype


# MARK: 3. Array creation
# # a = np.array(2, 3, 4)    # This is WRONG!
# b = np.array([2, 3, 4])    # This is correct.
#
# # Complex number
# c = np.array([[1, 2], [3, 4]], dtype=complex)
#
# # All 0 matrix. 4 * 3 matrix.
# d = np.zeros((3, 4))
# # `float64` type by default.
# dType = d.dtype
#
# # Designate dtype upon initialization.
# e = np.ones((3, 4), dtype=np.int64)
# # `int64`.
# eType = e.dtype
#
# # Uninitialized matrix. Value is unpredictable.
# f = np.empty((3, 4))
# # `float64` (seems to be the default type).
# fType = f.dtype


# MARK: 4. Array initialization 2
# # [0:5]
# a = np.arange(5)
# aType = a.dtype    # int64
#
# # Start (included), end (EXCLUDED), step
# b = np.arange(0, 3, 0.5)    # [0. 0.5 1. 1.5 2. 2.5]
# bType = b.dtype    # float64
#
# This is quite weird 😂...
# c = np.arange(0, 2.8, 0.5)    # [0. 0.5 1. 1.5 2. 2.5]
# cType = c.dtype    # float64


# MARK: 5
# # Start (included), end (INCLUDED), numbers count
# a = np.linspace(0, 2, 6)    # [0. 0.4 0.8 1.2 1.6 2. ]
# aType = a.dtype    # float64
#
# b = np.linspace(0, 2, 3)    # [0. 1. 2.]
# bType = b.dtype    # float64 😱
#
# # This is handy when emulating functions (just like Matlab)
# x = np.linspace(0, 2 * np.pi, 100)
# y = np.sin(x)


# MARK: 6. Printing arrays
# a = np.arange(6)
# print(a)    # [0 1 2 3 4 5]
#
# b = np.arange(6).reshape(2, 3)
# print(b)    # [[0 1 2] \n[3 4 5]]
#
# # Printing very large arrays.
# veryLargeArray = np.arange(10000)
# print(veryLargeArray)    # [   0    1    2 ... 9997 9998 9999]
# np.set_printoptions(threshold=sys.maxsize)
# print(veryLargeArray)    # This prints every value.


# MARK: Final statement for breakpoint 😂.
print("Quitting...")