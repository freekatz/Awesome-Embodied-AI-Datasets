# SACSoN


## Introduction

SACSoN is a vision-based robot navigation framework designed to achieve socially unobtrusive behavior in dynamic human environments by minimizing counterfactual perturbations to human intended trajectories. Its core innovation lies in training a control policy that uses only RGB images (without depth/LiDAR) to predict pedestrian dynamics and plan collision-free paths while preserving natural human motion patterns. Key components include:

HuRoN Dataset:

Autonomously collected via deployed data capture systems in real-world human spaces (e.g., office corridors, shopping malls).

Contains 120+ hours of synchronized RGB video, pedestrian trajectories, and robot states, capturing diverse interactions (e.g., avoidance, group movement, abrupt direction changes).

Counterfactual Perturbation Minimization:

Trains a pedestrian forward dynamics model to predict human motion under hypothetical robot interventions.

Optimizes navigation policies to reduce trajectory deviations caused by robot presence (e.g., minimizing human path deflection by 63% compared to traditional RL methods).

Zero-Shot Generalization:

Validated in 5 unseen environments (e.g., hospitals, campuses), achieving 92% navigation success with human discomfort events reduced by 5.7× vs. social-SLAM baselines.



## Homepage

[Visit the dataset homepage](https://sites.google.com/view/SACSoN-review)


## Task Description

Mobile robot navigates pedestrian-rich environments (e.g. offices, school buildings etc.) and runs a learned policy that may interact with the pedestrians.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 10           |
| Depth Cams                     | 1           |
| Has Camera Calibration                     | True           |
| Has Proprioception                     | False           |
| Has Suboptimal                     | False           |
| License                     | MIT           |
| Rgb Cams                     | 2           |
| Robot Morphology                     | Wheeled Robot           |
| Scene Type                     | Hallways           |
| Wrist Cams                     | 0           |


