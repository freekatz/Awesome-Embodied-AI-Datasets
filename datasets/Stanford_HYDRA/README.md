# Stanford HYDRA


## Introduction

HYDRA is an advanced imitation learning (IL) framework designed to address the critical challenge of state distribution shift in robotic control policies. Traditional IL methods suffer from compounding errors during execution when encountering unseen states, primarily due to inconsistent action predictions in expert demonstrations. HYDRA overcomes this by introducing a hybrid action space with two levels of temporal abstraction:

Sparse High-Level Waypoints: For coarse-grained control in free space (e.g., moving toward a coffee machine).

Dense Low-Level Actions: For fine-grained manipulation during contact-rich tasks (e.g., inserting a coffee pod).
The policy dynamically switches between these abstractions at test time, enabling adaptive control without sacrificing flexibility. Additionally, HYDRA employs action relabeling during waypoint phases to standardize low-level actions (e.g., ensuring consistent paths for reaching objects), reducing behavioral inconsistencies in the dataset by 40%.

Evaluated across seven challenging simulated and real-world tasks—including long-horizon activities like coffee brewing and toasting—HYDRA outperforms prior IL methods by 30–40% in success rates, achieving up to 80% success in complex real-world manipulation.



## Homepage

[Visit the dataset homepage](https://sites.google.com/view/hydra-il-2023)


## Task Description

The robot performs the following tasks in corresponding environment: making a cup of coffee using the keurig machine; making a toast using the oven; sorting dishes onto the dish rack.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 10           |
| Depth Cams                     | 0           |
| Episodes                     | 960           |
| File Size                     |  40.64 GB           |
| Gripper                     | Default           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| Language Annotations                     | Templated           |
| Rgb Cams                     | 2           |
| Robot                     | Franka           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top, Kitchen (also toy kitchen)           |
| Wrist Cams                     | 1           |


