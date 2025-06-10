# DLR Wheelchair Shared Control


## Introduction

This work tackles the challenge of training robotic policies on physical systems with minimal interaction time and robust safety guarantees, addressing traditional reinforcement learning’s (RL) reliance on extensive simulation or risky real-world trials that pose hardware damage risks; by combining safety-aware exploration and sparse reward designs, it enables efficient learning of complex manipulation tasks within minutes, featuring key innovations such as task-centric safety constraints (real-time torque monitoring to enforce tilt/spillage limits in pouring tasks and geometric path certificates to avoid collisions in fixture placement), sample efficiency achieving task proficiency in 65 episodes (∼16 minutes) for pouring and 75 episodes (∼17 minutes) for fixture placement—10× faster than model-free RL baselines—and sim-to-real elimination that bypasses simulators entirely to avoid dynamics mismatch issues.


## Homepage

[Visit the dataset homepage](https://ieeexplore.ieee.org/document/9341156)


## Task Description

The robot grasps a set of different objects in a table top and a shelf.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 5           |
| Depth Cams                     | 0           |
| Episodes                     | 92233           |
| File Size                     |  1670.00 GB           |
| Gripper                     | CLASH hand (https://www.dlr.de/rm/en/desktopdefault.aspx/tabid-8178/#gallery/35438)           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | True           |
| Language Annotations                     | Templated           |
| Rgb Cams                     | 1           |
| Robot                     | Franka           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top, shelf           |
| Wrist Cams                     | 0           |


