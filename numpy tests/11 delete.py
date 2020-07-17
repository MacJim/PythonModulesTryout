# np.delete

import numpy as np


def test1():
    x = np.arange(8)
    x = np.expand_dims(x, 1)
    print(x)

    y = np.delete(x, [3, 4, 5], axis=0)
    print(y)

    z = np.delete(x, np.array([1, 2, 3]), axis=0)
    print(z)


def test2():
    x = np.arange(8).reshape(2, -1)
    print(x)

    y = np.delete(x, [1], axis=0)
    print(y)

    z = np.delete(x, [1, 2], axis=1)
    print(z)


# test1()
test2()
