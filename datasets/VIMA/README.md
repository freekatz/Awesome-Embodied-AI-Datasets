# VIMA


## Introduction

VIMA-BENCH is a comprehensive benchmark designed to train and evaluate embodied AI agents capable of processing multimodal prompts (text, images, videos). Built on the Ravens robot simulator, it offers 17 task templates spanning six task specifications:

Task Types: Simple object manipulation, visual goal reaching, novel concept grounding, one-shot video imitation, visual constraint satisfaction, and visual reasoning .

Scale: Over 1,000 procedurally generated task instances and 650K expert demonstration trajectories .

Evaluation: A rigorous 4-level protocol tests generalization across:

Placement (randomized object positions)

Combinatorial (novel object-attribute combinations)

Novel Objects (unseen textures/3D models)

Novel Tasks (entirely new prompt templates) .

Data Modalities: RGB images (top-down/front views), object segmentation masks, bounding boxes, and high-level actions (e.g., "pick and place") .

The benchmark enables scalable training of transformer-based agents like VIMA, which achieved 2.9× higher zero-shot success rates than prior methods under equivalent conditions .



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
| License                     | Apache 2.0           |
| Rgb Cams                     | 2           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 0           |


