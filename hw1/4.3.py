import numpy as np

M = np.array([
    [0, 0, 1/2, 1/2, 1/2],
    [0, 0, 1/2, 1/2, 0],
    [1/3, 1/2, 0, 0, 0],
    [1/3, 1/2, 0, 0, 0],
    [1/3, 0, 0, 0, 0]
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

