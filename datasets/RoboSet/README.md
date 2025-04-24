# RoboSet


## Introduction

RoboSet is a dataset developed by the RoboSet project for robot-object interaction research. It contains 1,000 episodes of a PR2 robot interacting with household objects, including RGB images, depth data, and robot joint states. The dataset supports research in vision-based imitation learning and multi-object manipulation, with a focus on learning from human demonstrations. It is accompanied by evaluation scripts and pre-trained models, enabling comparisons across different vision-based robot learning approaches for tabletop tasks. While the dataset's license is not explicitly stated, it is primarily intended for academic use and emphasizes the integration of vision and proprioception for object manipulation tasks.


## Homepage

[Visit the dataset homepage](https://robopen.github.io/roboset/)


## Task Description

"The robot interacts with different objects in kitchen scenes. It performs articulated object manipulation of objects with prismatic joints and hinges. It wipes tables with cloth. It performs pick and place skills, and skills requiring precision like capping and uncapping."


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | Joint position           |
| Control Frequency                     | 5           |
| Depth Cams                     | 4           |
| Gripper                     | Robotiq 2F-85           |
| Has Camera Calibration                     | True           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | True           |
| Language Annotations                     | Natural           |
| Rgb Cams                     | 4           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top, Kitchen (also toy kitchen), Other Household environments           |
| Wrist Cams                     | 1           |


