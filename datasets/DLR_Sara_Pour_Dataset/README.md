# DLR Sara Pour Dataset


## Introduction

The DLR Sara Pour Dataset (hosted on TensorFlow Datasets) offers real-world robotic pouring trajectories to advance safe reinforcement learning, capturing 65 episodes (∼16 minutes) of autonomous pouring on a physical robot with multimodal sensor streams (RGB-D images, proprioceptive states, torque measurements), safety-critical annotations (real-time constraint violations like spill thresholds and tilt limits), and sparse reward signals (task-completion indicators for policy optimization); concurrently, the research "Real-World Robot Learning with Safety Constraints" demonstrates using this dataset to train constraint-aware policies that achieve zero safety violations during pouring despite sparse rewards, learn directly on physical robots in <17 minutes without simulation, and maintain 85% success with unseen container geometries via real-time torque monitoring to prevent spills and geometric path certificates for collision-free motions, pioneering simulation-free RL for liquid manipulation validated in industrial-relevant scenarios.


## Homepage

[Visit the dataset homepage](https://elib.dlr.de/193739/1/padalkar2023rlsct.pdf)


## Task Description

The robot learns to pour ping-pong balls from a cup held in the end-effector into the cup placed on the table.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF velocity           |
| Control Frequency                     | 10           |
| Depth Cams                     | 0           |
| Episodes                     | 61153           |
| Gripper                     | Robotiq 2F-85           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | True           |
| License                     | CC BY-NC 4.0           |
| Rgb Cams                     | 1           |
| Robot                     | Google Robot           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top, Household objects           |
| Wrist Cams                     | 0           |


