# Roboturk


## Introduction

RoboTurk Real Robot Dataset is a pioneering crowdsourced dataset for robotic imitation learning, curated by Stanford University's Visual Learning Lab led by Fei-Fei Li and Silvio Savarese. It comprises 2,144 real-world demonstrations collected from 54 remote operators via the RoboTurk platform, where users controlled physical Sawyer robot arms through smartphones or browsers to perform three manipulation tasks:

Object Search & Categorization: Locating and sorting scattered household items into target bins .

Block Stacking: Precise tower construction using colored cubes under varying spatial constraints .

Laundry Folding: Manipulating deformable textiles (e.g., towels, shirts) into folded configurations .

Each trajectory provides synchronized RGB video (640×480), joint states, gripper actions, and task success labels. With 111.25 hours of operation data, this dataset enables training robust visuomotor policies for complex tasks traditionally requiring expert demonstrations .



## Homepage

[Visit the dataset homepage](https://roboturk.stanford.edu/dataset_real.html)


## Task Description

Sawyer robots flattens laundry, builds towers from bowls and searches objects.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 10           |
| Depth Cams                     | 1           |
| Episodes                     | 39350           |
| File Size                     |  80.54 GB           |
| Gripper                     | Default           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| Language Annotations                     | Templated           |
| License                     | MIT           |
| Rgb Cams                     | 2           |
| Robot                     | Google Robot           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 0           |


