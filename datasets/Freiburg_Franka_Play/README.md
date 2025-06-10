# Freiburg Franka Play


## Introduction

TACO (Tool-Object Interaction with Dual-Hand Cooperation) is a large-scale real-world dataset capturing bimanual manipulation of tools and objects in daily activities. It provides 5.2 million RGB images from 12 third-person views and 1 egocentric view, covering 2,500 interaction sequences, 196 object meshes, and 131 distinct <tool, action, target object> triads (e.g., <spatula, stir, pot>). The dataset includes precise 4D annotations: hand-object mesh sequences, 2D segmentation masks, and marker-free images generated via an automated pipeline combining motion capture optimization and inpainting models. Designed for generalizable manipulation research, TACO introduces three benchmarks—Action Recognition, Motion Prediction, and Collaborative Grasp Synthesis—with specialized splits (S1-S4) to evaluate cross-category, geometric, and triad-compositional generalization. Experiments reveal significant gaps in state-of-the-art methods; for example, action recognition accuracy drops by 25% on unseen triads (S3 split), highlighting critical challenges in real-world deployment.



## Homepage

[Visit the dataset homepage](https://www.kaggle.com/datasets/oiermees/taco-robot)


## Task Description

"The robot interacts with toy blocks, it pick and places them, stacks them, unstacks them, opens drawers, sliding doors and turrns on LED lights by pushing buttons."


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 15           |
| Depth Cams                     | 2           |
| Episodes                     | 1355           |
| File Size                     |  3.53 GB           |
| Gripper                     | Custom 3D printed           |
| Has Camera Calibration                     | True           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| Language Annotations                     | Templated           |
| License                     | CC BY-SA 4.0           |
| Rgb Cams                     | 2           |
| Robot                     | xArm           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 2           |


