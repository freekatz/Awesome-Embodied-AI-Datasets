# QT-Opt


## Introduction

QT-Opt is a vision-based robotic manipulation dataset developed by researchers at Google and UC Berkeley. It focuses on closed-loop reinforcement learning for grasping tasks, containing over 580,000 real-world grasp attempts collected from a Sawyer robot. The dataset includes RGB camera observations, motor commands, and success/failure labels, enabling the training of deep neural networks for dynamic manipulation. QT-Opt's unique contribution lies in its ability to learn regrasping strategies, object probing, and dynamic responses to disturbances, achieving a 96% success rate on unseen objects. The dataset is released under the Open Data Commons Attribution License (ODC-BY), requiring attribution to the original authors while allowing modification and redistribution. It serves as a benchmark for vision-based RL research, demonstrating the potential of large-scale data collection for improving robotic dexterity and generalization.


## Homepage

[Visit the dataset homepage](https://arxiv.org/abs/1806.10293)


## Task Description

Kuka robot picking objects in a bin.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 10           |
| Depth Cams                     | 0           |
| Episodes                     | 200           |
| File Size                     |  0.59 GB           |
| Gripper                     | Default           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| Rgb Cams                     | 1           |
| Robot                     | Franka           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 0           |


