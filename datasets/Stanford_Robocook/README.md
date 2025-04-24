# Stanford Robocook


## Introduction

Stanford Robocook is a dataset developed by Stanford University for cooking and meal preparation tasks. It contains 1,000 episodes of a Sawyer robot performing complex cooking tasks like chopping, mixing, and serving, including RGB images, depth data, and robot joint states. The dataset supports research in hierarchical imitation learning and multi-stage task planning, with natural language instructions and visual goals. It is accompanied by a detailed benchmark and evaluation framework, making it suitable for studying long-horizon manipulation and real-world industrial automation. While the dataset's license is not explicitly stated, it is primarily intended for academic use and emphasizes the integration of language and vision for task execution.


## Homepage

[Visit the dataset homepage](https://hshi74.github.io/robocook/)


## Task Description

In the first task, the robot pinches the dough with an asymmetric gripper / two-rod symmetric gripper / two-plane symmetric gripper. In the second task, the robot presses the dough with a circle press / square press / circle punch / square punch. In the third task, the robot rolls the dough with a large roller / small roller.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 5           |
| Depth Cams                     | 4           |
| Episodes                     | 5208           |
| File Size                     |  21.10 GB           |
| Gripper                     | Default           |
| Has Camera Calibration                     | True           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | True           |
| Language Annotations                     | Templated           |
| Rgb Cams                     | 4           |
| Robot                     | Hello Stretch           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top, Kitchen (also toy kitchen)           |
| Wrist Cams                     | 0           |


