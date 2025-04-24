# Maniskill


## Introduction

Maniskill is a large-scale dataset developed by Haoshuai Group for robotic manipulation research. It contains over 100,000 episodes of simulated and real-world manipulation tasks, including pick-and-place, stacking, and tool use, with RGB images, depth data, and robot joint states. The dataset supports research in reinforcement learning, imitation learning, and cross-domain generalization, emphasizing the integration of vision and proprioception. It is released under the Apache 2.0 license, allowing free use and modification for research and development. Maniskill is accompanied by a detailed simulation environment and evaluation framework, making it a valuable resource for advancing robot learning in complex, dynamic environments.


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
| Rgb Cams                     | 2           |
| Robot                     | Sawyer           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 2           |


