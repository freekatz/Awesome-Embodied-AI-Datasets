# ASU TableTop Manipulation


## Introduction

In the field of robotic manipulation, achieving efficient training and good policy transferability 
has always been a major challenge. To address this problem, we propose the "Hierarchical Modularity" approach. 
This method decomposes complex tasks into reusable sub-modules and uses the "Supervised Attention" mechanism to 
dynamically combine these sub-modules to meet different task requirements. At the same time, we have constructed
an automated 3D object synthesis process and adopted a curriculum learning strategy to accelerate the model
training process. Experiments show that compared with traditional methods, such as BC-Z, our method increases the 
training speed by 30%-50% and improves the success rate of cross-robot task execution by 25%. We have conducted
numerous experiments in simulated environments (such as Franka, UR5) and on real UR5 robots, covering tasks such as 
obstacle avoidance and object relational placement, fully verifying the efficiency and generalization ability of 
this method. In addition, this method can also introspect the robot's decision-making process at runtime, improving 
the interpretability of the model and helping to further optimize the robot policy.



## Homepage

[Visit the dataset homepage](https://link.springer.com/article/10.1007/s10514-023-10129-1)


## Task Description

The robot interacts with a few objects on a table. It picks up, pushes forward, or rotates the objects.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 12.5           |
| Depth Cams                     | 0           |
| Episodes                     | 139           |
| File Size                     |  2.71 GB           |
| Gripper                     | Robotiq 2F-85           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| Language Annotations                     | Templated           |
| Rgb Cams                     | 1           |
| Robot                     | Spot           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 0           |


