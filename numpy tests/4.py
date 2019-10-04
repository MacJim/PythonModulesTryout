# Source: https://numpy.org/devdocs/user/quickstart.html

import numpy as np


# MARK: 1. Stacking arrays together.
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(a.dtype)    # int64

b = np.array([a[1], a[0]])

c = np.array([1, 2, 3])
d = np.array([6, 5, 4])

# Vertical and horizontal stacking.
print(np.vstack((a, b)), "\n")
print(np.row_stack((a, b)), "\n")

print(np.hstack([a, b]), "\n")
print(np.column_stack((a, b)), "\n")    # equivalent to hstack only for 2D arrays

print(np.vstack((c, d)), "\n")
print(np.row_stack((c, d)), "\n")

print(np.hstack((c, d)), "\n")
print(np.column_stack((c, d)), "\n")





