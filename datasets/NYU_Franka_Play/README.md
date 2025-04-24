# NYU Franka Play


## Introduction

NYU Franka Play is a dataset developed by NYU for robot learning through uncurated play data. It contains 365 episodes of a Franka Emika Panda robot interacting with a toy kitchen setup, including RGB images, depth data, and robot joint states. The dataset supports research in behavior generation and policy learning from unstructured, exploratory interactions, with a focus on learning from diverse and unlabeled data. While the dataset's license is not explicitly stated, it is primarily intended for academic use. NYU Franka Play is accompanied by evaluation scripts and pre-trained models, facilitating comparisons across different behavior cloning and policy learning methods.


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
| Rgb Cams                     | 2           |
| Robot                     | Franka           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Kitchen (also toy kitchen)           |
| Wrist Cams                     | 0           |


