# Imperial Wrist Cam


## Introduction

Robotic Platform Configuration:
The dataset is collected using a Sawyer robot equipped with a Robotiq 2F-85 gripper and a wrist-mounted RealSense D435 camera. The camera is positioned at a fixed offset of (7cm, 0cm, 18cm) relative to the end-effector tip coordinate system (x: forward, y: left, z: upward), with its optical axis aligned parallel to the negative z-axis for downward-facing observations.

Core Dataset Composition:
This real-world manipulation dataset focuses on wrist-camera perspectives during object interaction tasks. It provides synchronized streams of:

High-resolution RGB-D video (640×480 @ 30Hz)

Proprioceptive state data (joint positions/torques)

Gripper force/tactile measurements

Precise end-effector pose annotations

Research Applications:
Designed for visuomotor policy learning, the dataset enables:

Egocentric perception modeling: Studying viewpoint invariance in manipulation

Contact-rich control: Analyzing slip detection and force modulation

Sim2real transfer: Validating policies trained in simulation

Technical Infrastructure:
Integrated with the RLDS Dataset Builder ecosystem, it offers:

Standardized data loaders (TensorFlow/PyTorch)

ROS-compatible replay tools

Automatic metadata extraction



## Homepage

[Visit the dataset homepage](https://github.com/normandipalo/rlds_dataset_builder)


## Task Description

The robot interacts with different everyday objects performing tasks such as grasping, inserting, opening, stacking, etc.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 10           |
| Depth Cams                     | 0           |
| Episodes                     | 3847           |
| File Size                     |  89.33 GB           |
| Gripper                     | Robotiq 2F-85           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | False           |
| Has Suboptimal                     | False           |
| Language Annotations                     | Natural           |
| License                     | MIT           |
| Rgb Cams                     | 1           |
| Robot                     | Human           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 1           |


