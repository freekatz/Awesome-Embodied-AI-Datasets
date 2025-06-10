# CMU Franka Pick-Insert Data


## Introduction

Hierarchical Sensing for Robotic Manipulation proposes a novel framework for learning generalizable language-conditioned multi-task policies via spatial-temporal hierarchical sensing, addressing the challenge of balancing coarse-grained motion planning with reactive fine-grained manipulation by integrating multi-resolution sensing that enables agents to use multi-spatial-resolution sensing (hierarchical visual features at varying scales for global scene context and local object details to adjust trajectories precisely) and multi-temporal-resolution sensing (high-frequency feedback at 100Hz+ for real-time reactive control combined with low-frequency global reasoning at 5–10Hz for task planning); technically, it synergizes pre-trained vision-language models (VLMs) for low-frequency global feature extraction with lightweight non-pretrained networks for high-frequency local feedback adaptation, a dual-network architecture that reduces computational latency by 40% compared to monolithic models and demonstrates generalizability robust to visual/geometric object variations and dynamic interaction forces like sliding friction and collision recovery; validated across three manipulation domains—coarse tasks (e.g., long-range object fetching), precision tasks (e.g., gear insertion, cable routing), and dynamic tasks (e.g., catching moving objects, force-sensitive pouring)—experimental results show it achieves 2× higher average success rates versus state-of-the-art multi-task baselines like RT-1 and RoboFlamingo and superior zero-shot adaptation to unseen objects/environments.


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


