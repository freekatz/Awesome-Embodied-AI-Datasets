# DROID


## Introduction

DROID (Distributed Robot Interaction Dataset) is a large-scale, diverse robot manipulation dataset designed to advance the development of generalizable robotic policies. Collected over 12 months across 564 real-world environments (e.g., homes, offices, labs) in North America, Asia, and Europe, it comprises 76,000 demonstration trajectories (350 hours) covering 86 manipulation tasks—from object grasping and tool use to complex activities like appliance operation and clutter organization. This unprecedented scale and diversity are achieved through a distributed data collection framework involving 50 human operators and 18 standardized robot platforms across 13 institutions.

Core Technical Innovations:

Multi-Modal Sensing: Synchronized RGB-D streams (2 external + 1 wrist-mounted cameras), proprioceptive states (joint positions/velocities), and 6-DoF action trajectories sampled at 15 Hz, enabling closed-loop visuomotor policy training.

Scene-Task Diversity: Tasks span 10+ categories (e.g., "close waffle maker", "cook lentils") with randomized environmental perturbations (e.g., lighting changes, object nudging) to enhance robustness.

Language-Annotated Demos: Natural language instructions for each trajectory were crowdsourced via tasq.ai, supporting language-conditioned policy learning.

Hardware Standardization: All data collected on uniform Franka Emika Panda arms with Robotiq grippers, ensuring cross-institution consistency and reproducibility.

Validation & Impact:

Generalization Superiority: Policies trained on DROID achieve >40% higher success rates in unseen environments compared to those trained on Bridge V2 or RT-1 datasets, particularly under visual occlusions and object variations.

Real-World Deployment: Validated on mobile manipulators performing long-horizon tasks (e.g., "bake objects" and "clean tables") in cluttered home settings, demonstrating 85% task completion under dynamic disturbances.

Open Ecosystem: Public release includes dataset (CC-BY 4.0), policy training code, and hardware replication guides—accelerating community-driven robotics research.



## Homepage

[Visit the dataset homepage](https://droid-dataset.github.io/)


## Task Description

Various household manipulation tasks


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 15           |
| Depth Cams                     | 3           |
| Gripper                     | Robotiq 2F-85           |
| Has Camera Calibration                     | True           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | True           |
| Language Annotations                     | Natural           |
| License                     | CC BY-NC-SA 4.0           |
| Rgb Cams                     | 3           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top, Kitchen (also toy kitchen), Other Household environments, Hallways           |
| Wrist Cams                     | 1           |


