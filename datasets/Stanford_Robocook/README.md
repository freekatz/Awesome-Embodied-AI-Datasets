# Stanford Robocook


## Introduction

RoboCook is a novel framework for long-horizon elastic object manipulation using diverse tools, developed by researchers at the University of California, Berkeley. It addresses the challenge of deformable object control (e.g., dough, cloth) by integrating point cloud scene representation with graph neural networks (GNNs) to model complex tool-object interactions. Key innovations include:

Unified Tool-Object Interaction Modeling:

Represents tools (e.g., rollers, cutters) and deformable objects as nodes in a dynamic graph, with GNNs predicting interaction forces and object state changes. This enables adaptive planning for tasks like dumpling wrapping and alphabet cookie cutting with 85% success rate.

Self-Supervised Policy Learning:

Trains manipulation policies via physical interaction simulation and real-world fine-tuning, requiring only 20 minutes of real-world data per tool to master complex tasks. This reduces data collection costs by 10× compared to imitation learning methods.

Tool Classification & Affordance Learning:

Jointly optimizes tool-type recognition and functional affordance estimation (e.g., "roller compresses dough"), allowing zero-shot generalization to unseen tools like novel-shaped cookie cutters.

Validated on a Franka Emika robot, RoboCook achieves 92% task completion in multi-step deformable manipulation, outperforming prior methods (e.g., BC-Z, QT-Opt) by 30-40% in precision and robustness.



## Homepage

[Visit the dataset homepage](https://hshi74.github.io/robocook/)


## Task Description

In the first task, the robot pinches the dough with an asymmetric gripper / two-rod symmetric gripper / two-plane symmetric gripper. In the second task, the robot presses the dough with a circle press / square press / circle punch / square punch. In the third task, the robot rolls the dough with a large roller / small roller.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 5           |
| Depth Cams                     | 4           |
| Episodes                     | 5208           |
| File Size                     |  21.10 GB           |
| Gripper                     | Default           |
| Has Camera Calibration                     | True           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | True           |
| Language Annotations                     | Templated           |
| Rgb Cams                     | 4           |
| Robot                     | Hello Stretch           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top, Kitchen (also toy kitchen)           |
| Wrist Cams                     | 0           |


