import mujoco
import numpy as np

model = mujoco.MjModel.from_xml_path('src/robot_scene.xml')
data = mujoco.MjData(model)
mujoco.mj_forward(model, data)

base_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "mobile_base")
print(f"body pos: {model.body('mobile_base').pos}")
print(f"xpos: {data.xpos[base_id]}")
print(f"xipos (com): {data.xipos[base_id]}")

# Move and check
model.body("mobile_base").pos = np.array([0.235, 0.0, 0.06])
mujoco.mj_forward(model, data)
print(f"After move body pos: {model.body('mobile_base').pos}")
print(f"After move xpos: {data.xpos[base_id]}")

# Check end effector pos
gripper_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "gripper")
print(f"Gripper xpos: {data.xpos[gripper_id]}")

# Check apple pos
apple_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "apple")
print(f"Apple xpos: {data.xpos[apple_id]}")

dist = np.linalg.norm(data.xpos[gripper_id] - data.xpos[apple_id])
print(f"Dist gripper to apple: {dist}")
