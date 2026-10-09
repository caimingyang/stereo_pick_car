import mujoco
import numpy as np

model = mujoco.MjModel.from_xml_path('src/robot_scene.xml')
data = mujoco.MjData(model)

base_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "mobile_base")
PICK_DOCK_POS = np.array([0.0, 0.0, 0.06])
DRIVE_SPEED = 0.03

# Initialize
mujoco.mj_forward(model, data)
print(f"Initial pos: {data.xpos[base_id]}")

# Simulate _phase_drive_to_apple for 50 steps
for step in range(50):
    current_pos = data.xpos[base_id].copy()
    direction = PICK_DOCK_POS[:2] - current_pos[:2]
    dist = np.linalg.norm(direction)

    if dist < 0.05:
        print(f"Step {step}: Arrived at dock. Pos={current_pos}")
        break

    step_size = min(DRIVE_SPEED, dist)
    new_xy = current_pos[:2] + direction / dist * step_size
    model.body("mobile_base").pos = np.array([new_xy[0], new_xy[1], PICK_DOCK_POS[2]])
    mujoco.mj_forward(model, data)

    if step % 5 == 0:
        print(f"Step {step}: pos={current_pos}, dist={dist:.4f}, new_xy={new_xy}")
else:
    print(f"Final pos: {data.xpos[base_id]}")
