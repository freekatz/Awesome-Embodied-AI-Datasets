# ConqHose


## Introduction

The Conq-Hose Manipulation Dataset offers a comprehensive collection of robotic interaction trajectories for learning dynamic control policies on deformable hose objects, capturing multimodal sensorimotor data during diverse tasks like hose coiling, routing, and plug insertion to address challenges in handling highly deformable objects under real-world constraints, with key features including multimodal sensing (synchronized RGB-D videos from static and wrist cameras, proprioceptive states, and 6-DoF end-effector action trajectories sampled at 100 Hz for closed-loop policy training), task diversity (10+ scenarios in industrial and domestic settings such as routing around obstacles, precise connector insertion, and coiling), physical variability (hose materials like silicone and rubber, lengths from 0.5–3 m, and environmental conditions like clutter and friction forces to enhance generalization), and an annotation schema with language-instruction labels (e.g., "Coil the hose tightly") and success/failure metrics for instruction-conditioned policy learning; designed for visuomotor policy training (e.g., diffusion policies, affordance-based RL), the dataset supports sim-to-real transfer (validated on UR5 and Franka robots with 85% success in unstructured environments) and efficient adaptation (reducing demonstration requirements by 60% compared to manual teleoperation).


## Homepage

[Visit the dataset homepage](https://sites.google.com/view/conq-hose-manipulation-dataset/home)


## Task Description

The robot grabs, lifts, and drags the end of a vacuum hose around in an office environment.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF velocity           |
| Control Frequency                     | 30           |
| Depth Cams                     | 0           |
| Gripper                     | Default           |
| Has Camera Calibration                     | True           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | True           |
| Language Annotations                     | Natural           |
| License                     | CC BY-NC 4.0           |
| Rgb Cams                     | 6           |
| Robot Morphology                     | Mobile Manipulator           |
| Scene Type                     | Other Household environments, Hallways           |
| Wrist Cams                     | 0           |


