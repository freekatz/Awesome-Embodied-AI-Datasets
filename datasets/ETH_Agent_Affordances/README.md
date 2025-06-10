# ETH Agent Affordances


## Introduction

For mobile robots, interacting with articulated objects remains a challenging yet critical task. To address this challenge, we propose a novel closed-loop control pipeline that integrates manipulation priors from affordance estimation with sampling-based whole-body control. We introduce the concept of affordance-aware prompts, which holistically capture an agent’s capabilities and embodiment. Our method demonstrates superior performance over state-of-the-art approaches conditioned solely on end-effector geometry. Furthermore, closed-loop affordance reasoning enables the agent to segment tasks into discontinuous motions and recover from failures or unexpected states. Finally, this pipeline achieves high success rates in real-world long-horizon mobile manipulation tasks—specifically, opening (71%) and closing (72%) oven doors.


## Homepage

[Visit the dataset homepage](https://ieeexplore.ieee.org/iel7/10160211/10160212/10160747.pdf)


## Task Description

The robot opens and closes an oven, starting from different initial positions and door angles.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 66.6           |
| Depth Cams                     | 1           |
| Episodes                     | 1804           |
| File Size                     |  356.50 GB           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | True           |
| Language Annotations                     | Templated           |
| License                     | CC BY-NC 4.0           |
| Rgb Cams                     | 0           |
| Robot                     | Franka           |
| Robot Morphology                     | Mobile Manipulator           |
| Scene Type                     | Kitchen (also toy kitchen)           |
| Wrist Cams                     | 0           |


