# TidyBot


## Introduction

TidyBot is a personalized robotic assistance framework developed by researchers from Princeton University, Stanford University, and Google, designed to enable household cleaning tasks (e.g., sorting laundry, tidying objects) through natural language instruction and user preference learning. Its core innovation leverages large language models (LLMs) like GPT-3 Davinci to infer generalized user preferences from minimal examples (e.g., "yellow shirts in drawers, dark purple shirts in closets"), achieving 91.2% accuracy on unseen objects in benchmark tests and 85% success rate in real-world deployments. Key components include:

Few-shot Preference Summarization:

LLMs convert user-provided object placement examples into generalized rules (e.g., "shirts → closet, socks → drawers"), bypassing costly data collection and model retraining.

Multimodal Perception Integration:

Combines CLIP for image classification and OWL-ViT for object detection to ground language instructions in visual scenes.

Real-World Task Execution:

Validated across 8 real-world scenarios (e.g., recycling cans, storing toys), each with 10 objects tested over 3 trials.

This approach demonstrates that LLMs' summarization capabilities—trained on internet-scale text data—can directly enable robotic generalization without task-specific fine-tuning.



## Homepage

[Visit the dataset homepage](https://tidybot.cs.princeton.edu/)


## Task Description

The robot puts each object into the appropriate receptacle based on user preferences


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | Our dataset specifies a target receptacle for each object           |
| Depth Cams                     | 0           |
| Gripper                     | Robotiq 2F-85           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | False           |
| Has Suboptimal                     | False           |
| Language Annotations                     | Our dataset specifies object placements in text form           |
| Rgb Cams                     | 0           |
| Robot Morphology                     | Mobile Manipulator           |
| Scene Type                     | Kitchen (also toy kitchen), Other Household environments, living room, bedroom, kitchen, pantry room           |
| Wrist Cams                     | 0           |


