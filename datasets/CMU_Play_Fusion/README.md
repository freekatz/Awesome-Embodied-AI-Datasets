# CMU Play Fusion


## Introduction

CMU Play Fusion is a dataset developed by Carnegie Mellon University for skill acquisition via diffusion from language-annotated play. It contains 135 episodes of a Stretch robot performing kitchen interactions, including RGB images, depth data, and robot joint states. The dataset supports research in hierarchical imitation learning and multi-stage task planning, with natural language instructions and visual goals. It is accompanied by a detailed benchmark and evaluation framework, making it suitable for studying long-horizon manipulation and real-world industrial automation. While the dataset's license is not explicitly stated, it is primarily intended for academic use and emphasizes the integration of language and vision for task execution.


## Homepage

[Visit the dataset homepage](https://play-fusion.github.io/)


## Task Description

The robot plays with 3 complex scenes: a grill with many cooking objects like toaster, pan, etc. It has to pick, open, place, close. It has to set a table, move plates, cups, utensils. And it has to place dishes in the sink, dishwasher, hand cups etc.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 5           |
| Depth Cams                     | 0           |
| Gripper                     | Robotiq hand-e           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| Language Annotations                     | Natural           |
| Rgb Cams                     | 1           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top, Kitchen (also toy kitchen)           |
| Wrist Cams                     | 0           |


