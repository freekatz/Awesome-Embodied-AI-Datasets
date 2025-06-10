# Maniskill


## Introduction

ManiSkill2 is a unified benchmark for learning generalizable robotic manipulation skills, powered by SAPIEN, designed to address the limitations of existing benchmarks, such as the lack of object-level topological and geometric variations, fully dynamic simulation, and native support for multiple manipulation tasks. ManiSkill2 includes 20 manipulation task families, over 2000 object models, and more than 4 million demonstration frames, covering stationary/mobile-base, single/dual-arm, and rigid/soft-body manipulation tasks with 2D/3D input data simulated by fully dynamic engines. The benchmark supports a wide range of algorithms, including classic sense-plan-act, reinforcement learning, imitation learning, etc., and supports various visual observations (point cloud, RGBD) and controllers (e.g., action type and parameterization). ManiSkill2 also empowers fast visual input learning, allowing a CNN-based policy to collect samples at about 2000 FPS with 1 GPU and 16 processes on a regular workstation. The codes for the simulator, environments, and baselines are open-source, and an online challenge is hosted for interdisciplinary researchers.


## Homepage

[Visit the dataset homepage](https://github.com/haosulab/ManiSkill2)


## Task Description

The robot interacts with different objects placed on the plane (ground). The tasks include picking an isolated object or an object from the clutter up and moving it to a goal position, stacking a red cube onto a green cube, inserting a peg into the box, assembling kits, plugging a charger into the outlet on the wall, turning on a faucet.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 20           |
| Depth Cams                     | 2           |
| Episodes                     | 9200           |
| File Size                     |  76.17 GB           |
| Gripper                     | Default           |
| Has Camera Calibration                     | True           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | True           |
| Language Annotations                     | Templated           |
| License                     | Apache 2.0           |
| Rgb Cams                     | 2           |
| Robot                     | Sawyer           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 2           |


