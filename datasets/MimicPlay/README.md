# MimicPlay


## Introduction

MimicPlay is a dataset developed by the MimicPlay project for human-robot imitation learning. It contains 2,000 episodes of a Franka Emika Panda robot performing object manipulation tasks guided by natural language instructions, including RGB images, depth data, and robot joint states. The dataset supports research in open-vocabulary language understanding and real-time robot control, with a focus on integrating language and vision for task execution. It is accompanied by evaluation scripts and pre-trained models, enabling comparisons across different human-robot interaction methods. While the dataset's license is not explicitly stated, it is primarily intended for academic use and emphasizes the integration of visual and language data for robot task understanding.


## Homepage

[Visit the dataset homepage](https://mimic-play.github.io/)


## Task Description

The robot interacts with various appliances in five different scenes, including a kitchen with an oven; a study desk with a bookshelf and lamp; flowers and a vase; toy sandwich making; and cloth folding. It opens the microwave and drawers; places a book on the shelf; inserts a flower into the vase; and assembles a sandwich.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | Operational space control (OSC), which is similar to Task space position control but OSC is impedance control with consideration of the mass matrix. OSC is also used by VIOLA.           |
| Control Frequency                     | 15           |
| Depth Cams                     | 0           |
| Gripper                     | Default           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | True           |
| Language Annotations                     | Dataset does not contain language instruction annotation           |
| Rgb Cams                     | 3           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 0           |


