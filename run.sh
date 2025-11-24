#!/bin/bash

python -m infinigen.datagen.manage_jobs --output_folder outputs/hello_world_0 --num_scenes 1 --specific_seed 0 \
--configs desert.gin simple.gin --pipeline_configs local_16GB.gin monocular.gin blender_gt.gin