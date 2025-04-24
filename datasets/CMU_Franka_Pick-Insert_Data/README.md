# CMU Franka Pick-Insert Data


## Introduction

CMU Franka Pick-Insert Data is a dataset developed by Carnegie Mellon University for pick-and-place and insertion tasks. It contains 500 episodes of a Franka Emika Panda robot manipulating objects in cluttered environments, including RGB images, depth data, and robot joint states. The dataset supports research in open-world model-based reinforcement learning and dynamic manipulation, with a focus on generalization to unseen objects and environments. It is accompanied by evaluation scripts and pre-trained models, enabling comparisons across different vision-based robot learning approaches for pick-and-place tasks. While the dataset's license is not explicitly stated, it is primarily intended for academic use and emphasizes the integration of vision and proprioception.


## Homepage

[Visit the dataset homepage](https://openreview.net/forum?id=WuBv9-IGDUA)


## Task Description

The robot tries to pick up different shaped objects placed in front of it. It also tries to insert particular objects into a cylindrical peg.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 20           |
| Depth Cams                     | 0           |
| Episodes                     | 378           |
| File Size                     |  7.13 GB           |
| Gripper                     | Default           |
| Has Camera Calibration                     | For a subset of the cameras           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| Language Annotations                     | Templated           |
| Rgb Cams                     | 2           |
| Robot                     | Franka           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 1           |


