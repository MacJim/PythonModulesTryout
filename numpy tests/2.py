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
# # Random value on [0, 1) of a specific dimension.
# a = np.random.random((2, 3))    # Height: 2, width: 3 matrix with random values.
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


# MARK: 5. Mean
# a = np.arange(30).reshape(-1, 5)
# print(a)
# print(a.shape)    # (6, 5)
# print(np.mean(a))    # 14.5 Computed for the flattened array by default.
# print(np.mean(a, axis=0))    # [12.5 13.5 14.5 15.5 16.5]
# print(np.mean(a, axis=1))    # [ 2.  7. 12. 17. 22. 27.]

# b = np.arange(8).reshape(2, 2, 2)
# print(b)
# print(b.shape)
# # The following results are all 2D arrays.
# print(np.mean(b, axis=0))
# print(np.mean(b, axis=1))
# print(np.mean(b, axis=2))

# c = np.arange(10).reshape(5, 2)
# print(c[:, :1])
# print(c.shape)
# print(c)
# print(np.mean(c, axis=0))
# print(np.mean(c, axis=1))


# MARK: 6. Standard deviation
# a = np.arange(30).reshape(-1, 5)
# print(a)
# print(np.std(a))    # 8.65544144839919 Computed for the flattened array by default.
# print(np.std(a, axis=0))    # [8.53912564 8.53912564 8.53912564 8.53912564 8.53912564]
# print(np.std(a, axis=1))    # [1.41421356 1.41421356 1.41421356 1.41421356 1.41421356 1.41421356]

# b = np.arange(30)
# print(np.std(b))    # 8.65544144839919


# MARK: 7. Add row / column to matrix
# a = np.arange(10).reshape(5, 2)
# print(a.shape)
# print(a)

# # MARK: 7-1
# b = np.zeros((a.shape[0], a.shape[1] + 1))
# b[:, :-1] = a
# print(b.shape)
# print(b)

# # MARK: 7-2
# c = np.zeros((a.shape[0], 1))
# d = np.append(a, c, axis=1)
# print(d.shape)
# print(d)