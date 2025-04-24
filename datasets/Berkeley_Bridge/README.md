# Berkeley Bridge


## Introduction

Berkeley Bridge is a large-scale dataset for robot learning, developed by UC Berkeley's RAIL Lab. It contains 60,096 trajectories across 24 environments, focusing on tasks like pick-and-place, pushing, and folding. The dataset includes natural language instructions, multiple camera views, and depth data, supporting open-vocabulary and multi-task learning methods. It is designed to facilitate research on scalable robot learning by providing extensive task and environment variability, enabling models to generalize across domains. Berkeley Bridge is released under the MIT license, allowing free use, modification, and distribution. The dataset is accompanied by pre-trained models and evaluation scripts, making it a valuable resource for accelerating research in imitation learning and offline reinforcement learning.


## Homepage

[Visit the dataset homepage](https://rail-berkeley.github.io/bridgedata/)


## Task Description

The robot interacts with household environments including kitchens, sinks, and tabletops. Skills include object rearrangement, sweeping, stacking, folding, and opening/closing doors and drawers.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 5           |
| Depth Cams                     | 1           |
| Episodes                     | 150           |
| File Size                     |  1.33 GB           |
| Gripper                     | Default           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | True           |
| Language Annotations                     | Natural           |
| Rgb Cams                     | 4           |
| Robot                     | xArm           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top, Kitchen (also toy kitchen), Other Household environments           |
| Wrist Cams                     | 1           |


