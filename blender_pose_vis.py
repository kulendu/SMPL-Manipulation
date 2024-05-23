import bpy
import pickle
import numpy as np 



pkl_path = './AMASS_pose.pkl'


# loading the pkl file
with open(pkl_path, 'rb') as f:
	pose_data = pickle.load(f)


print(pose_data.keys())

betas = pose_data['betas']
translations = pose_data['translations']
poses = pose_data['poses']


# creating an armature
def create_armature():
    bpy.ops.object.armature_add(enter_editmode=True)
    armature = bpy.context.object
    armature.name = 'SMPL_Armature'
    bpy.ops.object.mode_set(mode='EDIT')

    # adding bones
    for i in range(1, 24):
        bone = armature.data.edit_bones.new(f'Bone_{i}')
        bone.head = (0, 0, 0)
        bone.tail = (0, 1, 0)
    
    bpy.ops.object.mode_set(mode='OBJECT')

    return armature

 # Function to set pose on the armature
def set_pose(armature, pose, translation):
    bpy.ops.object.mode_set(mode='POSE')
    for i, bone in enumerate(armature.pose.bones):
        # Assuming pose contains joint rotations
        # For simplicity, applying rotation directly; adjust according to your data format
        rot = pose[i*3:(i+1)*3]
        bone.rotation_mode = 'XYZ'
        bone.rotation_euler = (rot[0], rot[1], rot[2])
    
    # Apply translation to the root bone
    root_bone = armature.pose.bones[0]
    root_bone.location = translation
    bpy.ops.object.mode_set(mode='OBJECT')

# Create armature and apply poses
armature = create_armature()

# Assuming we want to visualize the first pose
set_pose(armature, poses[0], translations[0])

# Optionally, animate over multiple frames
frame_start = 1
bpy.context.scene.frame_start = frame_start
bpy.context.scene.frame_end = len(poses)

for frame in range(len(poses)):
    bpy.context.scene.frame_set(frame + frame_start)
    set_pose(armature, poses[frame], translations[frame])
    armature.keyframe_insert(data_path='location', index=-1)
    for bone in armature.pose.bones:
        bone.keyframe_insert(data_path='rotation_euler', index=-1)

print("Poses have been loaded and visualized in Blender.")
