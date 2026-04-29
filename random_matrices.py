import numpy as np
from scipy.linalg import subspace_angles

angles = [np.degrees(subspace_angles(
    np.linalg.qr(np.random.randn(64, 27))[0],
    np.linalg.qr(np.random.randn(64, 27))[0]
)).mean() for _ in range(10000)]

print(f"Random baseline: {np.mean(angles):.2f}")