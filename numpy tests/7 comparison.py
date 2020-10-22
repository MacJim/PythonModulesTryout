# Numpy comparisons.

import sys

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
    """
    Element-wise comparisons.
    """
    a = np.arange(10).reshape(2, -1)
    b = np.flip(a, axis=1)

    print(f"a: {a}")    # [[0 1 2 3 4] [5 6 7 8 9]]
    print(f"b: {b}")    # [[4 3 2 1 0] [9 8 7 6 5]]

    print(f"a == b: {a == b}")    # [[False False  True False False] [False False  True False False]]
    print(f"a > b: {a > b}")    # [[False False False  True  True] [False False False  True  True]]
    print(f"a < b: {a < b}")    # [[ True  True False False False] [ True  True False False False]]
    

def test_element_wise_2():
    """
    Can compare different data types.
    """
    a = np.arange(10)
    b = np.arange(10, dtype=np.float32)
    c = np.arange(10, dtype=np.int32)

    print(f"a: {a.dtype}, {a}")    # int64, [0 1 2 3 4 5 6 7 8 9]
    print(f"b: {b.dtype}, {b}")    # float32, [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]
    print(f"c: {c.dtype}, {c}")    # int32, [0 1 2 3 4 5 6 7 8 9]
    # `repr`: The "official" string representation that can be used to recreate an object.
    # https://docs.python.org/3/reference/datamodel.html#object.__repr__
    print(f"repr: a: {repr(a[6])}, b: {b[6]}, c: {c[6]}")    # a: 6, b: 6.0, c: 6

    print(f"a > b: {a > b}")    # [False False False False False False False False False False]
    print(f"a == b: {a == b}")    # [ True  True  True  True  True  True  True  True  True  True] This is unexpected!
    print(f"a == c: {a == c}")    # [ True  True  True  True  True  True  True  True  True  True]
    print(f"b == c: {b == c}")    # [ True  True  True  True  True  True  True  True  True  True]


def test_element_wise_3():
    """
    Special case 1: Different shapes.

    DeprecationWarning: elementwise comparison failed; this will raise an error in the future.

    Must make sure they have the same shape before using `==`.
    """
    a = np.arange(10)
    c = np.arange(10).reshape(2, -1)
    d = np.arange(6)
    print(f"a == c: {a == c}")    # False
    print(f"a == d: {a == d}")    # False
    try:
        print(f"(a == c).all(): {(a == c).all()}")
    except:
        # exception: (<class 'AttributeError'>, AttributeError("'bool' object has no attribute 'all'"), <traceback object at 0x7fde6f979dc0>)
        print(f"(a == c).all() exception: {sys.exc_info()}")


def test_element_wise_4():
    """
    Special case 2: Empty array.

    DeprecationWarning: elementwise comparison failed; this will raise an error in the future.
    """
    a = np.arange(6)
    b = np.array([])
    c = np.array([])
    print(f"b shape: {b.shape}")
    print(f"a == b: {a == b}")    # False
    print(f"b == c: {b == c}")    # []


# MARK: - Whole array comparison
# https://stackoverflow.com/questions/10580676/comparing-two-numpy-arrays-for-equality-element-wise
def test_whole_1():
    """
    Compare using:

    - `==` and `all()`
    - `!=` and `any()`.

    `all()`: All elements along an axis is `True`.
    """
    a: np.ndarray = np.arange(10)
    b: np.ndarray = np.arange(10, dtype=np.float32)
    c: np.ndarray = np.arange(6, 16)

    print(f"(a == b).all(): {(a == b).all()}")    # True
    print(f"(a != b).any(): {(a != b).any()}")    # False
    print(f"(a == c).all(): {(a == c).all()}")    # False
    print(f"(a != c).any(): {(a != c).any()}")    # True


def test_whole_2():
    """
    Compare using `np.array_equal` and `np.array_equiv`.
    """
    a = np.arange(10)
    b = np.arange(10, dtype=np.float32)
    c = np.array([])
    d = np.arange(10).reshape(2, -1)
    e = np.array([a, a])

    print(f"array_equal(a, b): {np.array_equal(a, b)}")    # True
    print(f"array_equal(a, c): {np.array_equal(a, c)}")    # False
    print(f"array_equal(a, d): {np.array_equal(a, d)}")    # False

    print(f"array_equiv(a, b): {np.array_equiv(a, b)}")    # True
    print(f"array_equiv(a, d): {np.array_equiv(a, d)}")    # False
    print(f"array_equiv(a, e): {np.array_equiv(a, e)}")    # True


# MARK: - Float precision
def test_precision_1():
    """
    `float64` and `float32` values don't equal.
    """
    # 0.00001
    a = np.array([0.00001])    # float64
    b = np.array([0.00001], dtype=np.float32)
    c = np.array([0.00001], dtype=np.float32)
    d = c.astype(np.float64)

    print(f"a: {a}")    # [1.e-05]
    print(f"b: {b}")    # [1.e-05]
    print(f"c: {c}")    # [1.e-05]
    print(f"d: {d}")    # [9.99999975e-06]

    print(id(a), id(b), id(c))    # `b` and `c` have different IDs.
    print(f"repr: a: {repr(a.item())}, b: {repr(b.item())}, c: {repr(c.item())}, d: {repr(d.item())}")    # a: 1e-05, b: 9.999999747378752e-06, c: 9.999999747378752e-06, d: 9.999999747378752e-06 They certainly have different representations.
    print(f"Is Python's `float`: a: {isinstance(a.item(), float)}, b: {isinstance(b.item(), float)}, c: {isinstance(c.item(), float)}, d: {isinstance(d.item(), float)}")    # True, True, True, True TODO: Why? I think only `np.float64` should equal Python's `float`.

    print(f"a == b: {a == b}")    # [False]
    print(f"b == c: {b == c}")    # [ True]
    print(f"a == d: {a == d}")    # [False]

    # 0.0001
    g = np.array([0.0001])    # float64
    h = np.array([0.0001], dtype=np.float32)
    print(f"g == h: {g == h}")    # [False]
    print(f"repr: g: {repr(g.item())}, h: {repr(h.item())}")    # g: 0.0001, h: 9.999999747378752e-05

    # 0.001
    i = np.array([0.001])
    j = np.array([0.001], dtype=np.float32)
    print(f"i == j: {i == j}")    # [False]
    print(f"repr: i: {repr(i.item())}, j: {repr(j.item())}")    # i: 0.001, j: 0.0010000000474974513

    # 0.01
    k = np.array([0.01])
    l = np.array([0.01], dtype=np.float32)
    print(f"k == l: {k == l}")    # [False]
    print(f"repr: k: {repr(k.item())}, l: {repr(l.item())}")    # k: 0.01, l: 0.009999999776482582


# test_number_1()

# test_element_wise_1()
# test_element_wise_2()
# test_element_wise_3()
# test_element_wise_4()

test_whole_1()
# test_whole_2()

# test_precision_1()
