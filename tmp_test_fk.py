import sys
sys.path.insert(0, 'src')
import numpy as np
from robot_controller import forward_kinematics

q = np.array([0.0, 0.5, -1.2, 0.0, 0.8, 0.0])
T = forward_kinematics(q)
print(f"End effector pos (rel base): {T[:3, 3]}")
