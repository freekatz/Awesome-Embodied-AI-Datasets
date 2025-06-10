# UTokyo xArm Bimanual


## Introduction

The xArm Dual-Board Manipulation Dataset is a specialized robotic interaction dataset recorded in RLDS format, capturing single-arm cooperative manipulation of two planar boards by Kinova xArm robots. Key features include:

Visual Observations: Top-down RGB streams (640×480 @30Hz) documenting manipulation contexts;

Robot States: End-effector Cartesian poses (ee_cartesian_pos), joint angles (joint_positions), and gripper status;

Action Sequences: 6-DoF displacement increments + gripper commands ({0: open, 1: hold, 2: close});

Task Annotations: Phase labels (e.g., "board_alignment", "object_transfer")

Structured with strict RLDS hierarchical formatting (step→episode→metadata), the dataset preserves temporal integrity for training constrained-space bimanual-like policies.



## Homepage

[Visit the dataset homepage](https://github.com/frt03/rlds_dataset_builder/tree/dev/xarm)


## Task Description

The robots reach a towel on the table. They also unfold a wrinkled towel.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 10           |
| Depth Cams                     | 0           |
| Episodes                     | 1500           |
| File Size                     |  20.79 GB           |
| Gripper                     | Default           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| License                     | Apache 2.0           |
| Rgb Cams                     | 1           |
| Robot                     | Franka           |
| Robot Morphology                     | Bi-Manual           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 0           |


