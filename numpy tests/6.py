import numpy as np


# MARK: 1. Matrix comparison
# a = np.array([1.2, 1.3])
# b = np.array([1.2, 1.3])
# c = np.array([1.200000001, 1.2999999999])
# d = np.array([1.205, 1.295])

# print(np.allclose(a, b))    # True
# print(np.allclose(a, c))    # True
# print(np.allclose(a, d))    # False


# MARK: 2. Shuffle matrix
# a = np.arange(9).reshape(3, 3)
# print(a)
# np.random.shuffle(a)
# print(a)


# MARK: 3. Select random elements from array in order
a = np.arange(20).reshape(10, 2)
# indices = np.random.choice(a.shape[0], size=10)    # Allows duplicates.
indices = np.random.choice(a.shape[0], size=5, replace=False)    # Does not allow duplicates.
indices = np.sort(indices)
print(indices)
b = a[indices]
print(b)
