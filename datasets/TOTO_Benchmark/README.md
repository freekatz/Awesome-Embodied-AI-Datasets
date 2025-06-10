# TOTO Benchmark


## Introduction

TOTO (Train Offline, Test Online) is a pioneering remote robotics benchmark designed to overcome three critical limitations in real-world robot learning research: (1) high costs of robot hardware restricting accessibility, (2) irreproducible results due to lab-specific robot platforms, and (3) lack of internet-scale robotic datasets. It provides researchers with free access to shared physical robots (Franka Emika arms) and standardized manipulation datasets, enabling reproducible offline training and real-time online policy testing. Key innovations include:

Unified Hardware Interface:

Remote control of identical robots via cloud APIs, eliminating hardware discrepancies and supporting cross-platform policy transfer validation .

Diverse Task Datasets:

Curates 10,000+ demonstration trajectories for 5 manipulation tasks (e.g., block stacking, door opening, cloth folding), each with synchronized RGB-D videos, proprioceptive states, and action annotations in RLDS format .

Offline-to-Online Evaluation:

Validates algorithms first on offline datasets, then deploys to physical robots for real-world testing, reducing hardware costs by 90% while ensuring policy robustness in dynamic environments .

TOTO's infrastructure accelerates research in sample-efficient RL, achieving 3.1× faster convergence for algorithms like DiffClone (enhanced behavior cloning) compared to isolated lab setups .



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
| License                     | BSD 2           |
| Rgb Cams                     | 1           |
| Robot                     | Unitree A1           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 0           |


