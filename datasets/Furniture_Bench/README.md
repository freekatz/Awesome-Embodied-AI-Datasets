# Furniture Bench


## Introduction

Fundamental Challenge:
Furniture assembly represents a critical challenge in robotic manipulation, requiring integrated capabilities in long-horizon planning, dexterous control, and robust visual perception. Existing benchmarks often lack real-world physical interactions or standardized evaluation protocols, hindering reproducible research.

Benchmark Design:
FurnitureBench addresses this gap as a real-world robotic assembly benchmark, featuring:

Diverse Tasks: Five IKEA furniture items (e.g., square table, cabinet) with varying complexity, each requiring 30-60 assembly steps.

Rich Dataset: Over 550 hours of human teleoperation data, including RGB-D observations, proprioceptive states, and action trajectories.

Standardized Metrics: Success rates, task completion time, and smoothness of motion, with a focus on generalization across object categories and hardware configurations.

Key Findings:
Evaluation of state-of-the-art methods (e.g., RL, imitation learning) reveals significant performance gaps:

Imitation Learning: Achieves only 42% success rate due to error compounding in long sequences.

Reinforcement Learning: Struggles with sparse rewards, requiring >10k episodes for basic proficiency.

Hardware Variance: Policies trained on one robot show >60% performance drop when transferred to other platforms (e.g., Franka vs. UR5).

Community Impact:
The benchmark provides open-source resources:

Task definitions with furniture CAD models and assembly manuals

Simulation-to-real calibration tools

Pre-trained baseline models and leaderboards
This enables reproducible research toward automating daily activities like home assembly.



## Homepage

[Visit the dataset homepage](https://clvrai.github.io/furniture-bench/)


## Task Description

The robot assembles one of 9 3D-printed furniture models on the table, which requires grasping, inserting, and screwing.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF velocity           |
| Control Frequency                     | 10           |
| Depth Cams                     | 0           |
| Episodes                     | 50           |
| File Size                     |  0.33 GB           |
| Gripper                     | Default           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| Language Annotations                     | Templated           |
| License                     | MIT           |
| Rgb Cams                     | 2           |
| Robot                     | Cobotta           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 1           |


