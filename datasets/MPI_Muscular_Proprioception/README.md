# MPI Muscular Proprioception


## Introduction

MPI Muscular Proprioception is a dataset developed by the Max Planck Institute for muscular proprioception research. It contains 1,000 episodes of a Franka Emika Panda robot interacting with soft materials, including RGB images, depth data, and robot joint states. The dataset supports research in real-time adaptation and human-in-the-loop learning, with a focus on integrating human feedback during robot operation. It is accompanied by evaluation scripts and pre-trained models, enabling comparisons across different pouring and fluid manipulation approaches. While the dataset's license is not explicitly stated, it is primarily intended for academic use and emphasizes the study of deformable object manipulation.


## Homepage

[Visit the dataset homepage](https://arxiv.org/abs/2307.02654)


## Task Description

There is no task that the robot solves. It executes a combination of random multisine signals of target pressures, as well as fixed target pressures.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | Desired pressures for the artificial muscles           |
| Control Frequency                     | 500           |
| Depth Cams                     | 0           |
| Episodes                     | 18250           |
| File Size                     |  178.65 GB           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | True           |
| Rgb Cams                     | 0           |
| Robot                     | Franka           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | The robot is alone in the environment, there are no other objects in the workspace.           |
| Wrist Cams                     | 0           |


