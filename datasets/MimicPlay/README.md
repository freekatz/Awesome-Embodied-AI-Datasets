# MimicPlay


## Introduction

The MimicPlay dataset is designed to support research in long-horizon robotic manipulation through imitation learning. It comprises two primary components: human play data, consisting of video sequences of individuals freely interacting with their environment using their hands, used to train a goal-conditioned trajectory generation model for creating a latent plan space; and teleoperated robot demonstration data, typically around 20 demonstrations per task, used to train a low-level robot controller conditioned on latent plans. The dataset supports 14 long-horizon manipulation tasks, facilitating the development of efficient imitation learning algorithms with superior performance, robustness, and generalization to new tasks compared to existing methods.



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
| License                     | MIT           |
| Rgb Cams                     | 3           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 0           |


