import numpy as np

def slingshot_detect(state, accel, a_thresh, dist_thresh):
    max_accel = np.linalg.norm(accel, axis=1).max()
    max_dist = np.linalg.norm(state['positions'], axis=1).max()
    if max_accel > a_thresh:
        print(f"Acceleration slingshot detected at acceleration: {max_accel}")
        return True
    if max_dist > dist_thresh:
        print(f"Distance slingshot detected at distance: {max_dist}")
        return True
    return False