# Berkeley Autolab UR5


## Introduction

Berkeley Autolab UR5 is a dataset for robot learning, developed by UC Berkeley's Autolab. It contains 10,000 episodes of a UR5 robot performing pick-and-place tasks in a simulated environment, including RGB images, depth data, and robot joint states. The dataset supports research in visual servoing and dynamic control, with a focus on real-time adaptation to environmental changes. While the dataset's license is not explicitly stated, it is primarily intended for academic use. Berkeley Autolab UR5 includes annotations for object poses and task goals, making it suitable for training models to learn closed-loop control policies. The dataset is accompanied by a detailed simulation environment and evaluation framework, enabling systematic testing of robot learning algorithms.


## Homepage

[Visit the dataset homepage](https://sites.google.com/view/berkeley-ur5/home)


## Task Description

The data consists of 4 robot manipulation tasks: simple pick-and-place of a stuffed animal between containers, sweeping a cloth, stacking cups, and a more difficult pick-and-place of a bottle that requires precise grasp and 6DOF rotation


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 5           |
| Depth Cams                     | 1           |
| Episodes                     | 192           |
| File Size                     |  0.81 GB           |
| Gripper                     | Robotiq 2F-85           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| Language Annotations                     | Templated           |
| Rgb Cams                     | 2           |
| Robot                     | PR2           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 1           |


