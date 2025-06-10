# NYU ROT


## Introduction

ROT (Regularized Optimal Transport) is a novel imitation learning framework proposed by researchers at New York University, designed to overcome the data inefficiency and high interaction costs of traditional Inverse Reinforcement Learning (IRL) methods. It integrates Optimal Transport (OT)-based trajectory matching with adaptive behavior cloning regularization, enabling robots to achieve high-precision policy learning with minimal demonstrations. Key innovations include:

One-shot demonstration & one-hour online training: On real-world robotic manipulation tasks (e.g., object pouring, cup placement, hanger mounting), ROT achieves an average success rate of 90.1% with only one expert demonstration and one hour of online fine-tuning, outperforming behavioral cloning (36.1%) and adversarial IRL (14.6%) by significant margins.

7.8× faster imitation learning: Across 20 simulated tasks (DeepMind Control, OpenAI Robotics, Meta-world), ROT reaches 90% expert performance 7.8× faster than prior state-of-the-art methods by adaptively balancing trajectory matching rewards and BC regularization via Soft Q-Filtering.

Robustness to distribution shift: By initializing policies with BC pretraining and refining via OT-based IRL with self-tuned regularization, ROT mitigates exploration challenges and distribution shifts in high-dimensional observation spaces.



## Homepage

[Visit the dataset homepage](https://rot-robot.github.io/)


## Task Description

The robot arm performs diverse manipulation tasks on a tabletop such an box opening, cup stacking, and pouring, among others.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 3           |
| Depth Cams                     | 0           |
| Episodes                     | 480           |
| File Size                     |  12.34 GB           |
| Gripper                     | Default           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| Language Annotations                     | Templated           |
| Rgb Cams                     | 1           |
| Robot                     | xArm           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 0           |


