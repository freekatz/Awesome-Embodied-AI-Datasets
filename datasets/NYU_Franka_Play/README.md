# NYU Franka Play


## Introduction

Play-to-Policy (P2P) is a novel framework for learning robotic manipulation policies through unstructured human "play" data. Unlike traditional task-specific demonstrations, it collects diverse, free-form interactions (e.g., object tossing, stacking, or sliding) from real-world environments. This data trains a goal-conditioned policy via self-supervised learning, enabling zero-shot generalization to unseen tasks. Key innovations include:

Scalable data collection: Humans freely interact with objects without predefined tasks, capturing 10x more behavioral diversity than task-centric datasets.

Automatic goal extraction: Self-generated subgoals from play trajectories bypass manual annotation.

Real-world deployment: Validated on 10+ manipulation tasks (e.g., "sort colored blocks", "place cup on coaster") with 80%+ success rate on novel instructions.



## Homepage

[Visit the dataset homepage](https://play-to-policy.github.io/)


## Task Description

The robot interacts with a toy kitchen doing arbitrary tasks. It opens/closes the microwave door, opens/closes the oven door, turns the stove knobs, and moves the pot between the stove and the sink.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF velocity           |
| Control Frequency                     | 3           |
| Depth Cams                     | 2           |
| Episodes                     | 812           |
| Gripper                     | Default           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| License                     | CC BY 4.0           |
| Rgb Cams                     | 2           |
| Robot                     | Franka           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Kitchen (also toy kitchen)           |
| Wrist Cams                     | 0           |


