# QUT Dexterous Manpulation


## Introduction

RLDS Dataset Builder is an open-source tool designed to simplify the creation and management of standardized datasets for reinforcement learning (RL) and sequential decision-making tasks. As part of the broader RLDS ecosystem developed by Google Research, it enables researchers to:

Record interactions between agents and environments in a lossless format, preserving temporal relationships (e.g., step sequences and episode boundaries).

Automate metadata annotation for custom fields (e.g., object states, task-specific metrics), ensuring compatibility with algorithms like offline RL and imitation learning.

Export datasets directly to TensorFlow Datasets (TFDS) for global sharing, enabling one-line loading via tfds.load() and integration with PyTorch/Numpy workflows.

Support diverse data sources, including synthetic agents (via EnvLogger) and human demonstrations (via RLDS Creator web tools).



## Homepage

[Visit the dataset homepage](https://github.com/fedeceola/rlds_dataset_builder)


## Task Description

The robot performs some tasks in a tabletop setting. It sorts dishes and objects, cooks and serves food, sets the table, throws away trash paper, rolls dices, waters plants, stacks toy blocks.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 30           |
| Depth Cams                     | 0           |
| Episodes                     | 276           |
| File Size                     |  47.83 GB           |
| Gripper                     | Default           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| Language Annotations                     | Natural           |
| License                     | CC BY 4.0           |
| Rgb Cams                     | 2           |
| Robot                     | MobileALOHA           |
| Robot Morphology                     | Mobile Manipulator           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 1           |


