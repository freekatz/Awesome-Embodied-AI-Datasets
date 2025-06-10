# QUT Dynamic Grasping


## Introduction

Dynamic Grasping Dataset is a specialized robotic manipulation dataset designed to advance research in real-time object grasping under motion. It contains 812 successful trajectories collected using a Franka Panda robotic arm interacting with objects on a programmable XY motion platform. Key features include:

Dynamic Object Movement: Objects are transported at variable speeds (0.1–0.5 m/s) along randomized trajectories via a CoreXY motion platform (3D-printable design with open-source components), simulating real-world scenarios like conveyor belts or moving targets.

Multi-modal Sensing: Each trajectory provides synchronized RGB-D video (640×480 @30Hz), joint states, end-effector poses, and binary grasp success labels, stored in RLDS-compatible format to preserve temporal integrity of step sequences.

Task Diversity: Covers 15 object categories (e.g., cubes, cylinders, irregular shapes) with varying textures and masses, requiring adaptive grasp strategies to compensate for object acceleration and slip.

This dataset serves as a benchmark for testing robust visuomotor policies in dynamic environments, enabling reproducible evaluation of offline RL and imitation learning algorithms.



## Homepage

[Visit the dataset homepage](https://github.com/krishanrana/rlds_dataset_builder)


## Task Description

The robot grasps an object that moves around continuously and randomly along the XY plane.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 30           |
| Depth Cams                     | 0           |
| Episodes                     | 11830           |
| File Size                     |  18.73 GB           |
| Gripper                     | Default           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| License                     | CC BY 4.0           |
| Rgb Cams                     | 3           |
| Robot                     | Jackal           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 2           |


