# TidyBot


## Introduction

TidyBot is a dataset developed by Princeton University for household cleaning tasks. It contains 570 episodes of a PR2 robot performing cleaning tasks like sweeping and mopping, including RGB images, depth data, and robot joint states. The dataset supports research in hierarchical imitation learning and multi-stage task planning, with natural language instructions and visual goals. It is accompanied by a detailed benchmark and evaluation framework, making it suitable for studying long-horizon manipulation and real-world industrial automation. While the dataset's license is not explicitly stated, it is primarily intended for academic use and emphasizes the integration of language and vision for task execution.


## Homepage

[Visit the dataset homepage](https://tidybot.cs.princeton.edu/)


## Task Description

The robot puts each object into the appropriate receptacle based on user preferences


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | Our dataset specifies a target receptacle for each object           |
| Depth Cams                     | 0           |
| Gripper                     | Robotiq 2F-85           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | False           |
| Has Suboptimal                     | False           |
| Language Annotations                     | Our dataset specifies object placements in text form           |
| Rgb Cams                     | 0           |
| Robot Morphology                     | Mobile Manipulator           |
| Scene Type                     | Kitchen (also toy kitchen), Other Household environments, living room, bedroom, kitchen, pantry room           |
| Wrist Cams                     | 0           |


