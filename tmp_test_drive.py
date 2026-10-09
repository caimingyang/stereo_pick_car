import mujoco
import numpy as np

model = mujoco.MjModel.from_xml_path('src/robot_scene.xml')
data = mujoco.MjData(model)

base_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_BODY, "mobile_base")
print(f"Initial body pos: {model.body('mobile_base').pos}")
print(f"Initial xpos: {data.xpos[base_id]}")

model.body("mobile_base").pos = np.array([0.0, 0.0, 0.06])
mujoco.mj_forward(model, data)
print(f"After set body pos: {model.body('mobile_base').pos}")
print(f"After xpos: {data.xpos[base_id]}")
