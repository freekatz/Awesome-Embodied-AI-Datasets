# Columbia PushT Dataset


## Introduction

Columbia PushT Dataset is a robotics dataset developed by Columbia University for vision-based manipulation tasks. It contains 1,647 real-world trajectories of a UR5 robot pushing T-shaped blocks into target positions, with RGB images, depth data, and robot joint states. The dataset is designed to support research in diffusion-based policy learning, particularly for long-horizon tasks requiring precise control. It is released under the MIT license, allowing free use and modification for academic and commercial purposes. Columbia PushT Dataset is accompanied by evaluation scripts and pre-trained models, making it a valuable resource for studying visuomotor policy learning and dynamic adaptation in physical robots.


## Homepage

[Visit the dataset homepage](https://github.com/columbia-ai-robotics/diffusion_policy)


## Task Description

The robot pushes a T-shaped block into a fixed goal pose, and then move to an fixed exit zone.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 10           |
| Depth Cams                     | 0           |
| Episodes                     | 70           |
| File Size                     |  0.14 GB           |
| Gripper                     | 3D printed stick           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| Rgb Cams                     | 5           |
| Robot                     | xArm Bimanual           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 1           |


