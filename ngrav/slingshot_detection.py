import numpy as np

def slingshot_detect(accel, a_thresh):
    max_accel = np.linalg.norm(accel, axis=1).max()
    if max_accel > a_thresh:
        return True
    return False