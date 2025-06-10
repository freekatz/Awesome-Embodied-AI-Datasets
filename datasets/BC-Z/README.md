# BC-Z


## Introduction

The BC-Z dataset is a large-scale robotic imitation learning benchmark developed collaboratively by Google, Everyday Robots, UC Berkeley, and Stanford University. It addresses the fundamental challenge of enabling vision-based robotic manipulation systems to generalize to unseen tasks through scalable data-driven learning. Trained on 25,877 diverse manipulation scenarios spanning 100 distinct tasks, BC-Z captures 125 hours of expert demonstrations collected from 12 robots operated by 7 human teleoperators. Its core innovation lies in supporting zero-shot task generalization—robots can execute novel tasks conditioned solely on high-level task descriptors (e.g., natural language embeddings or human demonstration videos) without task-specific retraining. This capability is enabled by a flexible multi-task policy architecture that learns 7-DoF control strategies adaptable to heterogeneous task representations. By integrating real-world complexity (e.g., object interactions, environmental variations), BC-Z provides a critical foundation for advancing robust and generalizable robotic manipulation. The dataset is publicly available under the CC BY-NC 4.0 license for non-commercial research use.


## Homepage

[Visit the dataset homepage](https://www.kaggle.com/datasets/google/bc-z-robot/discussion/309201)


## Task Description

The robot attempts picking, wiping, and placing tasks on a diverse set of objects on a tabletop, along with a few challenging tasks like stacking cups on top of each other.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 10           |
| Depth Cams                     | 0           |
| Episodes                     | 120           |
| File Size                     |  17.27 GB           |
| Gripper                     | Default           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | True           |
| Language Annotations                     | Templated           |
| License                     | CC BY 4.0           |
| Rgb Cams                     | 1           |
| Robot                     | Franka           |
| Robot Morphology                     | Mobile Manipulator           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 0           |


