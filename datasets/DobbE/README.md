# DobbE


## Introduction

Dobb-E: On Bringing Robots Home is an open-source framework designed to enable rapid learning of household manipulation tasks via data-driven imitation learning, addressing the critical challenges of scarce real-world training data and complexity in adapting to diverse domestic environments through two key components: The Stick, a low-cost hardware tool using iPhone sensors and 3D-printed parts to collect human demonstrations in real homes, capturing multimodal data (RGB-D, motion, depth) at 100 Hz for high-fidelity task recording without specialized equipment, and Home Pretrained Representations (HPR), a visual foundation model trained on 13 hours of data from 22 New York City homes that generalizes across environments by encoding household-specific features (e.g., lighting variations, clutter) to reduce task-specific retraining; in deployment, Dobb-E learns new tasks in 20 minutes (5 minutes of user demonstration with The Stick and 15 minutes of model fine-tuning to adapt HPR to the target environment), validated across 10 homes and 109 tasks (e.g., opening air fryers, arranging cushions) with an 81% success rate in unseen home settings—outperforming lab-trained baselines by >40%—and robustness to real-world challenges like strong shadows and novice-user demonstration variability.



## Homepage

[Visit the dataset homepage](https://github.com/notmahi/dobb-e)


## Task Description

The demo collector uses the Stick to collect data from 7 tasks, including door/drawer opening/closing, handle grasping, pick and place, and random play data.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 3.75           |
| Depth Cams                     | 1           |
| Gripper                     | Hello Robot Dex Wrist           |
| Has Camera Calibration                     | True           |
| Has Proprioception                     | False           |
| Has Suboptimal                     | False           |
| Language Annotations                     | Natural           |
| License                     | CC BY-NC 4.0           |
| Rgb Cams                     | 1           |
| Robot Morphology                     | Mobile Manipulator           |
| Scene Type                     | Kitchen (also toy kitchen), Other Household environments, Hallways           |
| Wrist Cams                     | 1           |


