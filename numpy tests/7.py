import numpy as np


x = np.array([1, 2, 3, 4, 4, 3], dtype=np.float32)
y = x > 2.0
z = np.argmax(x)

print(x)
print(y)    # [False False  True  True  True  True]
print(z)    # 3
