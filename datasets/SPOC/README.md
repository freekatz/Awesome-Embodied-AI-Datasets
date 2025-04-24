# SPOC


## Introduction

SPOC is a dataset developed by the SPOC project for scalable perception and object categorization tasks. It contains 1,500 episodes of a UR5 robot interacting with household objects, including RGB images, depth data, and robot joint states. The dataset supports research in vision-based imitation learning and multi-object manipulation, with a focus on learning from human demonstrations. It is accompanied by evaluation scripts and pre-trained models, enabling comparisons across different vision-based robot learning approaches for object categorization tasks. While the dataset's license is not explicitly stated, it is primarily intended for academic use and emphasizes the integration of vision and proprioception for object function understanding.


## Homepage

[Visit the dataset homepage](https://spoc-robot.github.io/)


## Task Description

The robot navigates in the environment and performs pick and place with open vocabulary descriptions.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | Joint position           |
| Control Frequency                     | 10           |
| Depth Cams                     | 2           |
| Gripper                     | Default           |
| Has Camera Calibration                     | True           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| Language Annotations                     | Scripted language but augmented with LLMs           |
| Rgb Cams                     | 2           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Kitchen (also toy kitchen), Other Household environments, Hallways, multi room environments           |
| Wrist Cams                     | 2           |


