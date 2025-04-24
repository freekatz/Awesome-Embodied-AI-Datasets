# RT-1 Robot Action


## Introduction

RT-1 Robot Action is a robotics dataset developed by Google Research, designed to enable robots to learn from diverse experiences across different tasks and environments. The dataset contains over 130,000 episodes of real-world robot actions collected from a fleet of robots over 17 months, covering more than 700 tasks such as grasping, pushing, and object repositioning. It emphasizes scalability and generalization by combining data from various robots, allowing models to learn transferable skills. The dataset is structured with RGB camera feeds, natural language instructions, and motor commands, supporting end-to-end control using the Robotics Transformer (RT-1) architecture. It is released under the permissive Apache 2.0 license, encouraging both academic and commercial use while promoting collaboration in the robotics community. RT-1 has demonstrated significant improvements in generalization to new tasks and environments, making it a valuable resource for advancing scalable robot learning research.


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
| Rgb Cams                     | 1           |
| Robot                     | Franka           |
| Robot Morphology                     | Mobile Manipulator           |
| Scene Type                     | Table Top, Kitchen (also toy kitchen)           |
| Wrist Cams                     | 0           |


