# Numpy comparisons.

import numpy as np


# MARK: - Compare with number
def test_number_1():
    x = np.array([1, 2, 3, 4, 4, 3], dtype=np.float32)

    print(f"x: {x}")
    print(f"x > 2.0: {x > 2.0}")    # [False False  True  True  True  True]
    print(f"x == 2.0: {x == 2.0}")    # [False  True False False False False]
    print(f"argmax(x): {np.argmax(x)}")    # 3


# MARK: - Element wise comparison
def test_element_wise_1():
    a = np.arange(10).reshape(2, -1)
    b = np.flip(a, axis=1)

    print(f"a: {a}")    # [[0 1 2 3 4] [5 6 7 8 9]]
    print(f"b: {b}")    # [[4 3 2 1 0] [9 8 7 6 5]]

    print(f"a == b: {a == b}")    # [[False False  True False False] [False False  True False False]]
    print(f"a > b: {a > b}")    # [[False False False  True  True] [False False False  True  True]]
    print(f"a < b: {a < b}")    # [[ True  True False False False] [ True  True False False False]]


# test_number_1()
test_element_wise_1()
