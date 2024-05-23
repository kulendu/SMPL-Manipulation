import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import torch
from smplx import SMPL
import pickle


# Path to the AMASS dataset file
amass_file = '/home/kulendu/SMPL-Manipulation/ACCAD/Male2MartialArtsExtended_c3d/Extended_1_stageii.npz'
smpl_model = '/home/kulendu/SMPL-Manipulation/SMPL_NEUTRAL.pkl'


data = np.load(amass_file)
print('Keys in the AMASS data - ', data.files)

poses = data['poses']
# print(len(poses))
translations = data['trans']
betas = data['betas']
print(len(betas))



pose_data = {
    'poses': poses,
    'translations': translations,
    'betas': betas
}




dumped_file = 'AMASS_pose.pkl'
with open(dumped_file, 'wb') as f:
    pickle.dump(pose_data, f)

print(f"Pose parameters have been extracted and saved to {dumped_file}.")