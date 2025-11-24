#!/usr/bin/env python3
import os
import shutil
import sys


def read_dirs_from_file(file_path):
    """Read directory names from a file, one per line."""
    if not os.path.isfile(file_path):
        print(f"Error: File not found - {file_path}")
        sys.exit(1)
    with open(file_path, "r") as file:
        return [line.strip() for line in file if line.strip()]


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <destination_dir>")
        sys.exit(1)

    dest = sys.argv[1]
    os.makedirs(dest, exist_ok=True)

    # Move data from the current directory structure to the destination
    # Example:
    # Move from: outputs/[TOP_DIRS]/[SCENE]/[SUB_DIRS]/camera_[0-9]/
    # To:       <destination_dir>/[SCENE]/[]

    # top directory names e.g. outputs/[TOP_DIRS]
    top_dirs = read_dirs_from_file("top_dirs.txt")

    # sub directory names e.g. outputs/[TOP_DIRS]/[ANY_SUBDIR]/[SUB_DIRS]
    # Below TOP_DIRS, the folder name for each camera is automatically filled,
    sub_dirs = read_dirs_from_file("sub_dirs_images.txt")

    # Uncomment to use different sub_dirs files
    # sub_dirs = read_dirs_from_file("sub_dirs_depths.txt")
    # sub_dirs = read_dirs_from_file("sub_dirs_depth_masks.txt")
    # sub_dirs = read_dirs_from_file("sub_dirs_masks.txt")
    # sub_dirs = read_dirs_from_file("sub_dirs_pointcloud.txt")

    # Process each top directory (result folders)
    for top in top_dirs:
        top_path = os.path.join(dest, top)
        if os.path.isdir(top_path):
            # Process each subdirectory directly under the top directory (scene folders)
            for scene in os.listdir(top_path):
                scene_path = os.path.join(top_path, scene)
                if os.path.isdir(scene_path):
                    # Process each subdirectory under the scene directory (e.g. frames/AO)
                    for sub in sub_dirs:
                        item_path = os.path.join(scene_path, sub)
                        if os.path.isdir(item_path):
                            # Process each camera directory (e.g. camera_0, camera_1)
                            for cameras in os.listdir(item_path):
                                cam_path = os.path.join(item_path, cameras)
                                if os.path.isdir(cam_path):
                                    # You can edit here to control the destination structure
                                    dest_cam_path = os.path.join(
                                        dest, top, sub, cameras
                                    )
                                    os.makedirs(dest_cam_path, exist_ok=True)
                                    # Move all files from the camera directory to the destination
                                    for item in os.listdir(cam_path):
                                        src_item = os.path.join(cam_path, item)
                                        dst_item = os.path.join(dest_cam_path, item)
                                        shutil.move(src_item, dst_item)


if __name__ == "__main__":
    main()
