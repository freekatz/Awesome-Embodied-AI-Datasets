# RT-1 Robot Action


## Introduction

RT-1 is a multi-task transformer model developed by Google Research, designed to enable real-time, vision-based robotic control through large-scale real-world data training. Trained on 130,000 demonstration episodes collected over 17 months from 13 Everyday Robots (EDR) platforms—each equipped with 7-DoF arms and mobile bases—the dataset captures diverse manipulation tasks across kitchen environments. Key features include:

Task Diversity: Covers 700+ tasks such as picking/placing objects, opening/closing drawers, inserting elongated items upright, pulling napkins, and opening cans, involving interactions with 1,000+ household objects under randomized lighting and camera views.

Language-Annotated Trajectories: Each episode is annotated with natural language instructions (e.g., "place the coffee pod into the machine"), enabling language-conditioned policy learning.

Multi-Modal Data: Synchronized RGB images, joint states, gripper actions, and binary success labels stored in a unified format for efficient transformer training.

RT-1’s architecture tokenizes visual inputs (via EfficientNet-B3) and robot actions into discrete bins, leveraging a TokenLearner module to compress spatial features and accelerate inference by 2.4×. This design achieves:

97% success rate on seen tasks and 73% on unseen task-object combinations, outperforming prior models (e.g., Gato, BC-Z) by >40% in generalization.

Robustness to disturbances: Maintains 89% accuracy under occlusion or object displacement scenarios.

Cross-domain data absorption: Effectively integrates simulation or heterogeneous robot data (e.g., Kuka bin-picking), improving transfer learning efficiency.



## Homepage

[Visit the dataset homepage](https://ai.googleblog.com/2022/12/rt-1-robotics-transformer-for-real.html)


## Task Description

Robot picks, places and moves 17 objects from the google micro kitchens.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 3           |
| Depth Cams                     | 1           |
| Episodes                     | 5100           |
| File Size                     |  110.00 GB           |
| Gripper                     | Default           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| Language Annotations                     | Templated           |
| License                     | Apache 2.0           |
| Rgb Cams                     | 1           |
| Robot                     | Franka           |
| Robot Morphology                     | Mobile Manipulator           |
| Scene Type                     | Table Top, Kitchen (also toy kitchen)           |
| Wrist Cams                     | 0           |


