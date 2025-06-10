# Berkeley Fanuc Manipulation


## Introduction

The FANUC Manipulation Dataset is a comprehensive vision-based robotic learning resource collected via a FANUC Mate 200iD robot, integrating multi-view visual data (third-person fixed and egocentric wrist-mounted 224×224 RGB videos), robot trajectory data (joint positions, gripper states, velocities, and Cartesian-space actions), and language task instructions (natural language commands for conditioning manipulation tasks), designed to advance imitation learning and vision-motor policy training by enabling visuomotor policy development (training closed-loop control models from visual inputs to actions), visual representation fine-tuning (adapting pre-trained models like ResNet and ViT to robotic domains), and instruction-conditioned generation (learning policies mapping language commands to robot behaviors), with a structured format supporting seamless integration with modern frameworks such as PyTorch and TensorFlow to facilitate cross-modal learning and sim-to-real transfer research.


## Homepage

[Visit the dataset homepage](https://sites.google.com/berkeley.edu/fanuc-manipulation)


## Task Description

A Fanuc robot performs various manipulation tasks. For example, it opens drawers, picks up objects, closes doors, closes computers, and pushes objects to desired locations.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 10           |
| Depth Cams                     | 0           |
| Episodes                     | 233000           |
| File Size                     |  765.00 GB           |
| Gripper                     | Default           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | True           |
| Language Annotations                     | Natural           |
| License                     | MIT           |
| Rgb Cams                     | 2           |
| Robot                     | Hello Stretch           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 1           |


