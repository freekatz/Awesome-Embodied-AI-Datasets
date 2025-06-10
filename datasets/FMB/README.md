# FMB


## Introduction

Functional Manipulation Benchmark is a fundamental capability for robots to interact with physical environments, yet existing benchmarks often focus on geometric goals (e.g., pose alignment) rather than functional outcomes. To bridge this gap, we introduce Functional Manipulation Benchmark (FMB), a comprehensive evaluation framework for robotic agents performing object-centric tasks requiring purpose-driven interactions. FMB integrates three core components: (1) Task diversity covering 50+ household objects with varied functional affordances (e.g., "pour from cup" vs. "close drawer"); (2) Physical realism simulated via quasi-static contact mechanics and frictional constraints; and (3) Goal-oriented metrics quantifying functional success through state changes (e.g., liquid volume transferred) rather than kinematic errors. Evaluations of 8 state-of-the-art manipulation policies reveal significant performance drops (average success rate: ≤42%) when functional requirements are prioritized over geometric precision, highlighting the need for embodied agents to reason about object functionality. FMB provides open-source task definitions, simulation environments, and leaderboards to accelerate research in functional manipulation.



## Homepage

[Visit the dataset homepage](https://functional-manipulation-benchmark.github.io/)


## Task Description

The robot interacts with diverse 3D printed objects, pick them up, reposition, and assemble them


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF velocity           |
| Control Frequency                     | 10           |
| Depth Cams                     | 4           |
| Gripper                     | Default           |
| Has Camera Calibration                     | True           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| Language Annotations                     | Templated           |
| License                     | CC BY-NC-SA 4.0           |
| Rgb Cams                     | 4           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 2           |


