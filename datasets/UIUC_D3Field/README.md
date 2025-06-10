# UIUC D3Field


## Introduction

D³Fields is a novel 3D scene representation framework for robotic manipulation, unifying dynamic modeling, semantic understanding, and geometric precision in a zero-shot generalizable paradigm. Its core innovation lies in constructing continuous descriptor fields that encode both geometric properties (e.g., signed distance to object surfaces) and semantic features (e.g., instance masks) by fusing multi-view 2D observations from foundation models (Grounding-DINO, SAM, XMem, DINOv2). Key capabilities include:

Flexible Goal Specification:

Enables task definition via 2D images from diverse sources (internet, user photos), establishing dense correspondences between robot workspace and target configurations without retraining .

Real-time Dynamics Tracking:

Projects arbitrary 3D points onto RGB-D streams to interpolate fused descriptors, updating object kinematics under deformation or occlusion at 15Hz .

Zero-Shot Policy Deployment:

Integrates with Model Predictive Control (MPC) for manipulation planning, achieving 92% success rate in household tasks (e.g., shoe tidying, debris collection) with unseen objects, outperforming Dense Object Nets by 37% in precision .



## Homepage

[Visit the dataset homepage](https://robopil.github.io/d3fields/)


## Task Description

The robot completes tasks specified by the goal image, including organizing utensils, shoes, mugs.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 1           |
| Depth Cams                     | 4           |
| Episodes                     | 24           |
| File Size                     |  0.02 GB           |
| Gripper                     | Robotiq 2F-85           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | True           |
| License                     | MIT           |
| Rgb Cams                     | 4           |
| Robot                     | TidyBot           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 0           |


