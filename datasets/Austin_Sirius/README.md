# Austin Sirius


## Introduction

Sirius enables collaborative manipulation tasks between humans and robots through shared autonomy. 
In this framework, robots execute actions autonomously while humans monitor performance and intervene via teleoperation to provide corrective guidance. 
Our core algorithm leverages deployment data to iteratively refine robot policies across successive rounds of policy learning, 
enhancing autonomy while minimizing human intervention. This closed-loop system bridges adaptive control and continuous improvement, 
advancing human-robot teamwork in complex real-world scenarios.

Key technical highlights:
- Shared Control: Seamlessly integrates human oversight with robot autonomy.
- Intervention-Driven Learning: Corrections via teleoperation directly inform policy updates.
- Iterative Policy Refinement: Data from each deployment cycle optimizes future autonomy.



## Homepage

[Visit the dataset homepage](https://ut-austin-rpl.github.io/sirius/)


## Task Description

The dataset comprises two tasks, kcup and gear. The kcup task requires opening the kcup holder, inserting the kcup into the holder, and closing the holder. The gear task requires inserting the blue gear onto the right peg, followed by inserting the smaller red gear.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF velocity           |
| Control Frequency                     | 20           |
| Depth Cams                     | 0           |
| Episodes                     | 2460           |
| File Size                     |  124.62 GB           |
| Gripper                     | Default           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| License                     | MIT           |
| Rgb Cams                     | 2           |
| Robot                     | Franka           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 1           |


