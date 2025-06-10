# KAIST Nonprehensile Objects


## Introduction

Problem Scope:
Non-prehensile object manipulation (e.g., pushing, toppling) requires rich contact patterns to transition objects to target states. Traditional methods rely on precise physical parameters (e.g., friction coefficients, center of mass), limiting adaptability in unstructured environments.

Technical Approach:
We propose a deep reinforcement learning (DRL) framework that bypasses prior physical knowledge. Its core innovations include:

Structured Action Space: Decouples contact point selection and motion control, enabling diverse contact patterns without handcrafted heuristics.

Curriculum Learning: Progressively increases task complexity (e.g., from sliding to toppling) to accelerate exploration.

Feedforward Policy Network: Reduces planning time to milliseconds via lightweight forward prediction.

Key Advantage:
The method achieves >90% success in simulation-to-real transfer for multi-contact tasks (e.g., pivoting irregular objects), outperforming model-based planners by 37% in scenarios with unknown dynamics.

Community Resource:
Integrated with the RLDS Dataset Builder ecosystem, providing:

Standardized data collection tools for real-world contact-rich manipulation

Pre-trained policies and simulation environments

Compatibility with ROS and PyTorch dataloaders



## Homepage

[Visit the dataset homepage](https://github.com/JaeHyung-Kim/rlds_dataset_builder)


## Task Description

The robot performs various non-prehensile manipulation tasks in a tabletop environment. It translates and reorients diverse real-world and 3d-printed objects to a target 6dof pose.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 10           |
| Depth Cams                     | 0           |
| Episodes                     | 135           |
| File Size                     |  0.71 GB           |
| Gripper                     | Default           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | True           |
| Language Annotations                     | Natural           |
| License                     | MIT           |
| Rgb Cams                     | 1           |
| Robot                     | Hello Stretch           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 0           |


