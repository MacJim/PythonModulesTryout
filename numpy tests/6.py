import numpy as np


# MARK: 1. Matrix comparison
a = np.array([1.2, 1.3])
b = np.array([1.2, 1.3])
c = np.array([1.200000001, 1.2999999999])
d = np.array([1.205, 1.295])

print(np.allclose(a, b))    # True
print(np.allclose(a, c))    # True
print(np.allclose(a, d))    # False

