import numpy as np

def collision_detect(positions, tolerance):
    # for few objects this will be fine
    diff = positions[np.newaxis, :, :] - positions[:, np.newaxis, :]
    dists = np.linalg.norm(diff, axis=2)
    np.fill_diagonal(dists, np.inf)
    if np.any(dists <= tolerance):
        print(f"Collision detected at tolerance: {tolerance}")
        return True
    return False