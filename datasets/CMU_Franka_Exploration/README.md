# CMU Franka Exploration


## Introduction

Human-World Model addresses the challenge of learning complex manipulation skills directly in the real world by leveraging internet-scale human video data, inspired by advancements in computer vision and natural language processing to enable robots to acquire generalizable behaviors from minimal interaction data (as few as 30 minutes per task), with core innovation in a structured human-centric action space based on visual affordances learned from human videos that capture human-object interactions (e.g., grasping, pushing) to provide priors for robotic manipulation; the framework includes an Affordance-Centric World Model pre-trained on diverse human videos to understand object interactions and physical causality (e.g., "a cup can be lifted when grasped") and predict environmental changes from actions, bridging human demonstrations to robot execution, and an Efficient Robot Adaptation component fine-tuned with ≤50 robot trajectories per task to ground robot actions in human-derived affordances, reducing exploration complexity and accelerating policy convergence; validated across 7 manipulation tasks (e.g., tool use, deformable object handling), the method achieves task generalization to unseen objects/environments (e.g., kitchen to office), data efficiency with a 90% success rate using 30x less data than RL baselines, and real-world deployability on UR5 and Franka Emika arms in cluttered scenes, unifying human priors with robot learning to pioneer scalable embodied intelligence.


## Homepage

[Visit the dataset homepage](https://human-world-model.github.io/)


## Task Description

Franka exploring kitchen environment, lifting knife and vegetable and opening cabinet.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 10           |
| Depth Cams                     | 0           |
| Episodes                     | 100           |
| File Size                     |  2.92 GB           |
| Gripper                     | Default           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | False           |
| Has Suboptimal                     | True           |
| Language Annotations                     | Templated           |
| License                     | CC BY-NC 4.0           |
| Rgb Cams                     | 1           |
| Robot                     | DLR SARA           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Kitchen (also toy kitchen)           |
| Wrist Cams                     | 0           |


