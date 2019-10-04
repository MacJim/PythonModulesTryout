import numpy as np


# MARK: 1. Vector operations.
# a = np.arange(20, 60, 10)
# b = np.arange(4)
#
# c = a - b
# print(c)    # [20 29 38 47]
#
# # Element wise multiplication, rather than matrix multiplication.
# print(b ** 2)    # [0 1 4 9]
# print(a * b)    # [  0  30  80 150]
#
# print(10 * np.sin(b))
#
# print(a < 35)    # [ True  True False False]


# MARK: 2. Matrix operations.
# i = np.array([[1, 0], [0, 1]])
# a = np.array([[4, 3], [2, 1]])
# b = np.array([[1, 2], [3, 4]])
#
# # Matrix multiplication.
# print(a @ b)
# print(i @ b)


# MARK: 3
# a = np.ones(3, dtype=np.int64)
# b = np.linspace(0, np.pi, 3)
#
# print(b.dtype)    # float64
#
# c = a + b
# print(c)
# print(c.dtype)    # float64
#
# # Complex number?
# d = np.exp(a * 1j)
# print(d)
# print(d.dtype)    # complex128

# MARK: 4
# # Random value on [0, 1).
# a = np.random.random((2, 3))
# print(a)
#
# # Element wise operations, rather than row / column wise operations 😂.
# print(a.sum())
# print(a.min())
# print(a.max())
#
# # Column / row wise operations
# # Axis: 0 column / 1 row
# b = np.array([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ])
# print(b.sum(axis=0))    # [15 18 21 24]
# print(b.min(axis=1))    # [1 5 9]
# # Cumulative sum (interesting)
# print(b.cumsum(axis=1))    # [[ 1  3  6 10]\n [ 5 11 18 26]\n [ 9 19 30 42]]
