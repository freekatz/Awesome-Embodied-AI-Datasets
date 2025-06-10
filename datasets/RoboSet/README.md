# RoboSet


## Introduction

RoboSet is a large-scale, multi-robot manipulation dataset curated by researchers at the University of Washington and NVIDIA, designed to advance cross-platform policy learning and real-world skill transfer. It aggregates over 100,000 demonstration trajectories from 5 distinct robot platforms (including Franka Emika Panda, UR5, and xArm), covering 50+ manipulation tasks such as tool handling, deformable object manipulation, and precision assembly. Each trajectory provides synchronized multimodal data:

Sensor streams: RGB-D video (640×480 @30Hz), proprioceptive states, and force/torque readings .

Action annotations: Joint velocities, Cartesian end-effector commands, and gripper states .

Task metadata: Object categories, scene configurations, and success/failure labels .

Key innovations include:

Cross-robot generalization: Policies trained on RoboSet achieve 68% success rate on unseen robots, reducing domain adaptation costs by 60% compared to single-platform datasets .

Long-horizon task support: 20% of tasks involve multi-step objectives (e.g., "insert bolt → tighten nut → place cover"), enabling learning of complex action sequences .

Real-world noise robustness: Incorporates natural perturbations (e.g., human interruptions, lighting changes) to enhance policy resilience in unstructured environments .



## Homepage

[Visit the dataset homepage](https://robopen.github.io/roboset/)


## Task Description

"The robot interacts with different objects in kitchen scenes. It performs articulated object manipulation of objects with prismatic joints and hinges. It wipes tables with cloth. It performs pick and place skills, and skills requiring precision like capping and uncapping."


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | Joint position           |
| Control Frequency                     | 5           |
| Depth Cams                     | 4           |
| Gripper                     | Robotiq 2F-85           |
| Has Camera Calibration                     | True           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | True           |
| Language Annotations                     | Natural           |
| License                     | CC BY 4.0           |
| Rgb Cams                     | 4           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top, Kitchen (also toy kitchen), Other Household environments           |
| Wrist Cams                     | 1           |


