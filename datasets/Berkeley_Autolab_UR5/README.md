# Berkeley Autolab UR5


## Introduction

The Berkeley-UR5 Project is an integrated research initiative focused on advancing robotic manipulation capabilities using UR5 collaborative robots, with particular emphasis on deformable object handling, human-robot interaction, and imitation learning in unstructured environments. Developed at the University of California, Berkeley, this project leverages the UR5's lightweight design (5kg payload) and 6-DoF flexibility to execute complex tasks such as cloth folding, cable rearrangement, and precision handover operations. Its core innovation lies in a multi-modal learning framework combining imitation learning (e.g., Multi-level Kernelized Movement Primitives) and goal-conditioned visual policies (e.g., Transporter Networks), enabling the robot to generalize skills from limited demonstrations to novel scenarios—such as adapting fabric manipulation strategies to varying textile stiffness or scaling handover trajectories across workspace regions. The project further provides open-source simulation benchmarks (e.g., DeformableRavens) with 12 standardized tasks for training and evaluating deformable object manipulation, alongside real-world datasets capturing UR5 kinematic states and visual observations for reproducibility. By bridging sim-to-real gaps through modular hardware interfaces and reinforcement learning pipelines, Berkeley-UR5 serves as a foundational platform for research in adaptive industrial automation and domestic service robotics.


## Homepage

[Visit the dataset homepage](https://sites.google.com/view/berkeley-ur5/home)


## Task Description

The data consists of 4 robot manipulation tasks: simple pick-and-place of a stuffed animal between containers, sweeping a cloth, stacking cups, and a more difficult pick-and-place of a bottle that requires precise grasp and 6DOF rotation


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 5           |
| Depth Cams                     | 1           |
| Episodes                     | 192           |
| File Size                     |  0.81 GB           |
| Gripper                     | Robotiq 2F-85           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| Language Annotations                     | Templated           |
| License                     | CC BY 4.0           |
| Rgb Cams                     | 2           |
| Robot                     | PR2           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 1           |


