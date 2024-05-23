import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import torch
from smplx import SMPL
import trimesh

# Path to the AMASS dataset file
amass_file = '/home/kulendu/SMPL-Manipulation/ACCAD/Male2MartialArtsExtended_c3d/Extended_1_stageii.npz'

# Load the dataset
data = np.load(amass_file)

print(data.files)

frame_index = 0
poses = data['poses'][frame_index]
betas = data['betas'][:10]
trans = data['trans'][frame_index]

smpl_model_path = '/home/kulendu/SMPL-Manipulation/SMPL_NEUTRAL.pkl'

# Load SMPL model
smpl = SMPL(model_path=smpl_model_path, gender='neutral', create_transl=False)

poses = poses[:72]

# Ensure betas have length 10
if len(betas) != 10:
    raise ValueError(f"Expected shape parameters (betas) of length 10, but got {len(betas)}")

# Convert pose and shape to tensors with float32 type
body_pose = torch.tensor(poses[3:], dtype=torch.float32).unsqueeze(0)  # Exclude the global orientation
global_orient = torch.tensor(poses[:3], dtype=torch.float32).unsqueeze(0)
betas = torch.tensor(betas, dtype=torch.float32).unsqueeze(0)
trans = torch.tensor(trans, dtype=torch.float32).unsqueeze(0)
faces = smpl.faces

# Generate body mesh from pose and shape
output = smpl(global_orient=global_orient, body_pose=body_pose, betas=betas)
vertices = output.vertices[0].detach().numpy()

print('No. of Frames:', len(data['poses']))

# Visualize the frame
mesh = trimesh.Trimesh(vertices, faces)
mesh.show()


