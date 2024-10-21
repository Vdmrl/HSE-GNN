import numpy as np

M = np.array([
    [4/9, 2/7, 1/8, 1/8, 1/5],
    [2/9, 3/7, 1/8, 1/8, 0],
    [1/9, 1/7, 3/8, 2/8, 1/5],
    [1/9, 1/7, 2/8, 3/8, 1/5],
    [1/9, 0, 1/8, 1/8, 2/5]
])

r_prev = np.array([0.2, 0.2, 0.2, 0.2, 0.2])
tolerance = 0.01
i = 1

while True:
    r_next = np.dot(M, r_prev)
    print(i, r_next)
    i += 1
    if np.linalg.norm(r_next - r_prev) < tolerance:
        break
    r_prev = r_next

