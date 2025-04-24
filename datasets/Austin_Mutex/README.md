# Austin Mutex


## Introduction

Austin Mutex is a dataset developed by the University of Texas at Austin's RPL Lab for multimodal task specification learning. It contains 5,000 episodes of a UR5 robot performing household tasks like stacking and sorting, including RGB images, depth data, and robot joint states. The dataset supports research in hierarchical policy learning and skill transfer, with a focus on learning from prior demonstrations and adapting to new tasks. It is released under the MIT license, allowing free use and modification for academic and commercial purposes. Austin Mutex is accompanied by evaluation scripts and pre-trained models, enabling comparisons across different skill-based imitation learning methods.


## Homepage

[Visit the dataset homepage](https://ut-austin-rpl.github.io/MUTEX/)


## Task Description

The Mutex dataset involves a diverse range of tasks in a home environment, encompassing pick and place tasks like "putting bread on a plate," as well as contact-rich tasks such as "opening an air fryer and putting a bowl with dogs in it" or "taking out a tray from the oven and placing bread on it."


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 20           |
| Depth Cams                     | 0           |
| Episodes                     | 660103           |
| File Size                     |  1390.00 GB           |
| Gripper                     | Default           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| Language Annotations                     | Natural Language annotations generate with GPT4 and followed by human correction.           |
| Rgb Cams                     | 2           |
| Robot                     | UR5           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 1           |


