# Stanford MaskVIT Data


## Introduction

Stanford MaskVIT Data is a robotics dataset developed by Stanford University for video prediction and robot planning. It contains 1,000 episodes of a Sawyer robot performing object manipulation tasks, including RGB images, depth data, and robot joint states. The dataset supports research in masked visual pre-training for video prediction, with a focus on learning from unstructured, real-world interactions. It is released under the Apache 2.0 license, allowing free use and modification for academic and commercial purposes. Stanford MaskVIT Data is accompanied by evaluation scripts and pre-trained models, enabling comparisons across different video prediction and robot planning approaches.


## Homepage

[Visit the dataset homepage](https://arxiv.org/abs/2206.11894)


## Task Description

The robot randomly pushes and picks objects in a bin, which include stuffed toys, plastic cups and toys, etc, and are periodically shuffled.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | null, actions are run until robot comes to rest near the target position (quasistatic assumption)           |
| Depth Cams                     | 0           |
| Episodes                     | 7328           |
| File Size                     |  1.39 GB           |
| Gripper                     | 3D printed grippper from https://github.com/robertocalandra/sawyer-printable           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | True           |
| Rgb Cams                     | 1           |
| Robot                     | RC Car           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 0           |


