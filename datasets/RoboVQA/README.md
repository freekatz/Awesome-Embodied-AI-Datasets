# RoboVQA


## Introduction

RobotVQA is a novel visual question answering (VQA) framework designed to bridge scene understanding and robotic action planning. It generates structured scene graphs from RGB-D inputs, enabling robots to interpret complex environments and execute task-oriented queries (e.g., "Which object is graspable on the left shelf?"). Key innovations include:

Scene graph generation: Converts raw sensor data into semantic graphs with nodes (objects/attributes) and edges (spatial/functional relations), supporting zero-shot transfer from synthetic (VirtualHome) to real-world scenes (72.3% relation prediction accuracy) .

Actionable VQA: Trains transformer-based models to answer manipulation-focused questions (e.g., "Can the red block be stacked on the blue cylinder?") and output executable action sequences (e.g., [GRASP(red_block), PLACE_ON(blue_cylinder)]) .

Real-world validation: Deployed on UR5 robots, RobotVQA achieves 89% task success in object retrieval and assembly scenarios by grounding language commands in scene graphs .



## Homepage

[Visit the dataset homepage](https://anonymous-robovqa.github.io/)


## Task Description

A robot or a human performs any long-horizon requests from a user within the entirety of 3 office buildings.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 10           |
| Depth Cams                     | 1           |
| Gripper                     | Default           |
| Has Camera Calibration                     | True           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| Language Annotations                     | Natural           |
| License                     | BSD 2           |
| Rgb Cams                     | 1           |
| Robot Morphology                     | 3 embodiments: single-armed robot, single-armed human, single-armed human using grasping tools           |
| Scene Type                     | Table Top, Kitchen (also toy kitchen), Other Household environments, Hallways, anything within 3 entire office buildings           |
| Wrist Cams                     | 0           |


