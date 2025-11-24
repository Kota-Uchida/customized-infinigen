# run in command line: blender your_scene.blend --background --python set_focal_length.py
import bpy

# Set the desired focal length in millimeters
desired_focal_length = 80.0

camera = bpy.data.objects[
    "camera_0_0"
]  # Replace 'Camera' with your camera's name if different

camera.data.lens = desired_focal_length

bpy.ops.wm.save_mainfile()
