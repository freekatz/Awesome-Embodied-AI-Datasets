# QT-Opt


## Introduction

QT-Opt is a scalable deep reinforcement learning framework developed by Google Brain in 2018, designed to enable robots to learn closed-loop vision-based manipulation skills through large-scale real-world data. Its core innovation lies in combining off-policy Q-learning with distributed optimization, allowing robots to continuously adjust grasping strategies based on real-time visual feedback (e.g., RGB camera inputs). Trained on 580,000+ real-world grasp attempts across 1,000 diverse objects, QT-Opt achieves a 96% success rate on unseen objects—outperforming supervised learning baselines by 18% and reducing error rates by 5×. Key advancements include:

Self-supervised skill emergence: Robots autonomously learn complex behaviors like regrasping, object repositioning, and obstacle displacement without manual programming.

Cross-domain robustness: Adapts to dynamic disturbances (e.g., human interference) and varying object textures/shapes using only monocular RGB vision.

Scalable data collection: Leverages distributed training across 7 robots over 4 months, with GPU-accelerated optimization reducing sample complexity by 40%.



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
| License                     | BSD 3           |
| Rgb Cams                     | 1           |
| Robot                     | Franka           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 0           |


