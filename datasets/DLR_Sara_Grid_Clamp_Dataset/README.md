# DLR Sara Grid Clamp Dataset


## Introduction

Real-World Robot Learning with Safety Constraints addresses the challenge of training robotic policies on physical systems with minimal interaction time and strong safety guarantees, overcoming traditional RL’s need for extensive simulation or risky real-world trials by integrating safety-aware exploration and simple reward designs to enable efficient learning of complex manipulation tasks within minutes; core innovations include task-centric safety constraints (e.g., real-time force/torque monitoring for pouring to limit vessel tilt/spillage and geometric path certificates for collision-free grid fixture placement), sample efficiency achieving task proficiency in 65 episodes (∼16 minutes) for pouring and 75 episodes (∼17 minutes) for fixture placement—10× faster than model-free RL baselines, minimalist sparse reward design (e.g., successful pour volume, fixture alignment accuracy) to reduce engineering complexity, and sim-to-real elimination via direct real-world training to avoid dynamics mismatch; validated with zero collisions in 140+ executions on a 7-DoF arm, 85% success adapting to unseen container shapes/fixture layouts, and demonstrated in manufacturing tasks like precision assembly and liquid handling, the approach ensures hardware safety and accelerates industrial deployment.


## Homepage

[Visit the dataset homepage](https://www.researchsquare.com/article/rs-3289569/v1)


## Task Description

The robot learns to place the grid clamp in the grids on the table.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF velocity           |
| Control Frequency                     | 10           |
| Depth Cams                     | 0           |
| Episodes                     | 451           |
| Gripper                     | Robotiq 2F-140           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | True           |
| License                     | CC BY 4.0           |
| Rgb Cams                     | 1           |
| Robot                     | ViperX Bimanual           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top, Workshop environment           |
| Wrist Cams                     | 0           |


