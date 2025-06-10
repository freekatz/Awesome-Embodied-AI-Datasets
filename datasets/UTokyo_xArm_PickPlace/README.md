# UTokyo xArm PickPlace


## Introduction

The xArm Dual-Board Manipulation Dataset is an RLDS-formatted benchmark for single-arm cooperative manipulation of dual planar surfaces. It features:

Constrained Task Design:

Records robotic interactions with two 30×30cm boards (15cm apart), emulating bimanual tasks like inter-board object transfer and alignment calibration.

Multimodal Trajectories:

Synchronizes top-view RGB (640×480 @30Hz), end-effector poses (ee_cartesian_pos), joint states, and discrete gripper commands ({0:open, 1:hold, 2:close}).

Phase Annotation:

Labels 5 operational phases (approach→alignment→transfer→release→reset) for hierarchical policy learning.

Research Utility:

Enables precision control validation (±2mm accuracy) in spatially constrained scenarios (e.g., lab automation, electronics assembly).



## Homepage

[Visit the dataset homepage](https://github.com/frt03/rlds_dataset_builder/tree/dev/xarm)


## Task Description

The robot picks up a white plate, and then places it on the red plate.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 10           |
| Depth Cams                     | 0           |
| Episodes                     | 196           |
| File Size                     |  15.82 GB           |
| Gripper                     | Default           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| License                     | Apache 2.0           |
| Rgb Cams                     | 4           |
| Robot                     | Kinova Gen3           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 1           |


