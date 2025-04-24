# MobileALOHA


## Introduction

MobileALOHA is a dataset developed by the MobileALOHA project for mobile robot manipulation tasks. It contains 100,000 episodes of a mobile manipulator performing household tasks, including RGB images, depth data, and robot joint states. The dataset supports research in language-conditioned policy learning and cross-task generalization, with a focus on training models to adapt to new tasks without additional demonstrations. It is accompanied by evaluation scripts and pre-trained models, enabling comparisons across different zero-shot imitation learning methods. While the dataset's license is not explicitly stated, it is primarily intended for academic use and emphasizes the integration of language and vision for task execution.


## Homepage

[Visit the dataset homepage](https://mobile-aloha.github.io/)


## Task Description

The robot interacts with diverse appliances in a real kitchen and indoor environments. It wipes spilled wine, stores a heavy pot to be inside wall cabinets, calls an elevator, pushes chairs, and cooks shrimp.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | Joint position           |
| Control Frequency                     | 50           |
| Depth Cams                     | 0           |
| Gripper                     | Default           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| Language Annotations                     | Templated           |
| Rgb Cams                     | 3           |
| Robot Morphology                     | Mobile Manipulator           |
| Scene Type                     | Table Top, Kitchen (also toy kitchen), Other Household environments, Hallways           |
| Wrist Cams                     | 0           |


