# VIMA


## Introduction

VIMA is a dataset developed by VIMA Labs for vision and language navigation tasks. It contains 1,000 episodes of a mobile robot navigating complex environments, including RGB images, depth data, and natural language instructions. The dataset supports research in open-vocabulary language understanding and real-time robot control, with a focus on integrating language and vision for task execution. It is accompanied by evaluation scripts and pre-trained models, enabling comparisons across different human-robot interaction methods. While the dataset's license is not explicitly stated, it is primarily intended for academic use and emphasizes the integration of visual and language data for robot navigation tasks.


## Homepage

[Visit the dataset homepage](https://vimalabs.github.io/)


## Task Description

The robot is conditioned on multimodal prompts (mixture of texts, images, and video frames) to conduct tabletop manipulation tasks, ranging from rearrangement to one-shot imitation.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | Primitive skills (pick-place and push)           |
| Control Frequency                     | null due to use of primitive skills           |
| Depth Cams                     | 0           |
| Gripper                     | Suction cup and spatula           |
| Has Camera Calibration                     | True           |
| Has Proprioception                     | False           |
| Has Suboptimal                     | False           |
| Language Annotations                     | Multimodal (image + language) templated instructions           |
| Rgb Cams                     | 2           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 0           |


