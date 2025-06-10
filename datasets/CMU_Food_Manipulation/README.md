# CMU Food Manipulation


## Introduction

Playing with Food tackles the core challenge of modeling the diverse material properties of deformable foods in robotic food manipulation by proposing a multimodal sensory approach where robots interact with and "play" with food items like slicing and squeezing to learn discriminative representations of their physical characteristics, integrating a robotic arm with synchronized vision, audio, and proprioceptive sensors under the ROS framework to collect a rich dataset of 21 unique food types with varied textures and deformability, using which a cross-modal embedding network is trained to fuse visual, proprioceptive, and audio inputs and encode material similarities via a triplet loss formulation, with evaluations showing these embeddings significantly improve material classification (e.g., distinguishing tofu from cheese), shape robustness (e.g., recognizing sliced vs. whole vegetables), and generalization to unseen foods while enabling material-aware parameter tuning for downstream tasks like adaptive slicing force, and to accelerate food robotics innovation, the study open-sources the Food-Play Dataset—the first to combine multisensory interaction data with deformable food properties.


## Homepage

[Visit the dataset homepage](https://sites.google.com/view/playing-with-food/)


## Task Description

Robot interacting with different food items.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 10           |
| Depth Cams                     | 0           |
| Episodes                     | 450           |
| File Size                     |  1.26 GB           |
| Gripper                     | Default           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| Language Annotations                     | Templated           |
| License                     | CC BY-NC 4.0           |
| Rgb Cams                     | 3           |
| Robot                     | Franka           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 2           |


