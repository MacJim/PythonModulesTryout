# Source: https://numpy.org/devdocs/user/quickstart.html

import numpy as np


# MARK: 1. Universal Functions
# a = np.arange(10)
# print(a)
# print(np.exp(a))
# print(np.sqrt(a))


# MARK: 2. Indexing, slicing and iterating
# a = np.arange(10) ** 3
#
# print(a)
# print(a[2])
# print(a[2:5])
# print(a ** (1 / 3.))    # What does this do? Just a ^ (1 / 3) power 3 root.
#
# a[0:6:2] = 1000    # equivalent to a[:6:2] = -1000; from start to position 6, exclusive, set every 2nd element to -1000
# print(a)
#
# print(a[::-1])    # Reversed `a`


# MARK: 3. Multi-directional array
# a = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])
# print(a.shape)    # (3, 3)
#
# print(a[2, 1])    # 8
#
# print(a[0:2, 1])    # [2, 5] <- It's no longer a matrix, but a normal array!
# print(type(a[0:2, 1]))    # The type is still <class 'numpy.ndarray'> though...
#
# print(a[2])    # [7, 8, 9]
# print(a[2, :])    # [7, 8, 9]
# print(a[:, 2])    # [3, 6, 9]
#
# print(a[-1, :])    # The final row [7, 8, 9]. This is really Python styled!
#
# c = np.array( [[[  0,  1,  2],    # a 3D array (two stacked 2D arrays)
#                  [ 10, 12, 13]],
#                 [[100,101,102],
#                  [110,112,113]]])
# print(c.shape)    # (2, 2, 3)
#
# for aRow in c:
#     print(aRow)
#
# for anElement in c.flat:    # This treats the multi-directional array as a 1D array. `flat` seems to be only available to `for ` iterations.
#     print(anElement)


# MARK: 4. Shape Manipulation
# a = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [10, 11, 12]
# ])
# print(a.shape)
#
# # Transpose 😱.
# print(a.T)
#
# # Unravel and ravel actually have the same meaning...
# # Flattens a multi directional array into a 1D array. This can be very useful.
# print(a.ravel())    # [ 1  2  3  4  5  6  7  8  9 10 11 12]
#
# # `reshape` returns a copy while `resize` re-sizes in place.
# print(a.reshape(3, 4))
# # print(a.reshape(5, 5))    # This throws a `ValueError`
#
# a.resize(3, 4)
# print(a)


