# TOTO Benchmark


## Introduction

TOTO Benchmark is a robotics dataset developed for the Train Offline, Test Online (TOTO) competition at NeurIPS 2023, focusing on real-world robot learning tasks. The dataset includes over 100 human-teleoperated trajectories of pouring and scooping tasks collected from a Franka Emika Panda robot, with RGB images, natural language instructions, and robot joint states. It emphasizes the challenge of training models offline using expert demonstrations and evaluating them online on physical robots, requiring generalization to unseen scenarios. The dataset is released under the Apache 2.0 license, enabling both academic and commercial use while promoting reproducibility in robotics research. TOTO Benchmark serves as a critical resource for advancing offline RL and behavior cloning methods in real-world manipulation tasks.


## Homepage

[Visit the dataset homepage](https://toto-benchmark.org/)


## Task Description

The TOTO Benchmark Dataset contains trajectories of two tasks: scooping and pouring. For scooping, the objective is to scoop material from a bowl into the spoon. For pouring, the goal is to pour some material into a target cup on the table.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | Joint position           |
| Control Frequency                     | 30           |
| Depth Cams                     | 0           |
| Episodes                     | 20           |
| File Size                     |  0.05 GB           |
| Gripper                     | Default           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | True           |
| Rgb Cams                     | 1           |
| Robot                     | Unitree A1           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 0           |


