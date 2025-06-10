# Robonet


## Introduction

RoboNet is the first open database for sharing robotic experience across diverse platforms, initiated by researchers from Stanford University, UC Berkeley, and Google. It aggregates 15 million video frames from 7 distinct robot types (including Franka Emika Panda, Sawyer, and Kuka arms) performing manipulation tasks in varied tabletop environments. Each frame contains synchronized RGB images, joint states, gripper status, and force sensor readings, capturing autonomous interactions with 1,000+ household objects under randomized camera views and lighting conditions. Key innovations include:

Cross-platform generalization: Training on RoboNet enables policies to transfer skills across robots with different kinematics (e.g., from 7-DoF Sawyer to 6-DoF UR5), achieving 43.7% higher success rates in unseen home environments compared to single-robot datasets.

Data diversity amplification: By randomizing object textures, table appearances, and camera poses, RoboNet reduces domain gap between simulated and real-world deployment, cutting Sim2Real fine-tuning costs by 75%.

Support for predictive models: The dataset enables self-supervised learning of visual foresight models and inverse dynamics models, allowing robots to perform non-grasping tasks (e.g., object pushing) and handle novel objects without task-specific retraining.



## Homepage

[Visit the dataset homepage](https://www.robonet.wiki/)


## Task Description

The robot interacts with the objects in a bin placed in front of it


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF velocity           |
| Control Frequency                     | 1           |
| Depth Cams                     | 0           |
| Episodes                     | 415           |
| File Size                     |  8.85 GB           |
| Gripper                     | Default grippers + Weiss gripper (for sawyer)           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | True           |
| License                     | CC BY 4.0           |
| Rgb Cams                     | 3           |
| Robot                     | Fanuc Mate           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 0           |


