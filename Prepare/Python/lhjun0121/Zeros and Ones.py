import numpy as np

a = tuple(map(int, input().split()))
print(np.zeros(a, dtype = np.int32))
print(np.ones(a, dtype = np.int32))