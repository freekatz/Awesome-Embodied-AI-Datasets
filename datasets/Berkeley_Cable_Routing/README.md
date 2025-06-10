# Berkeley Cable Routing


## Introduction

Multistage Cable Routing through Hierarchical Imitation Learning tackles the challenge of enabling robots to perform complex multi-stage manipulation tasks like routing cables through a series of clips, which require handling deformable objects, closing visual perception loops, and executing extended sequential behaviors; traditional methods face cumulative failure rates in such tasks due to exponential diminishment of success probability with each primitive's error, so the proposed hierarchical imitation learning system includes high-level policies that select primitives from a low-level library to enable failure recovery via retries or controller switching, low-level visuomotor primitives trained from 1,442 demonstration trajectories for precise motor control, and interactive fine-tuning for rapid adaptation to novel scenarios like unseen clip placements through human interventions, with key innovation in compensatory primitive design that ensures robustness by having primitives compensate for each other’s imperfections rather than relying on individual performance, and evaluations demonstrating exceptional generalization to challenging clip variations, enabling failure recovery via autonomous retries and corrective actions, scalable data efficiency with training using only 257 end-to-end demonstrations by reusing low-level primitives, and real-world deployability validated on physical cable routing tasks requiring long-horizon planning.


## Homepage

[Visit the dataset homepage](https://sites.google.com/view/cablerouting/home)


## Task Description

The robot routes cable through a number of tight-fitting clips mounted on the table.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF velocity           |
| Control Frequency                     | 10           |
| Depth Cams                     | 0           |
| Episodes                     | 600           |
| File Size                     |  6.55 GB           |
| Gripper                     | Default           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| License                     | MIT           |
| Rgb Cams                     | 3           |
| Robot                     | Franka           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 2           |


