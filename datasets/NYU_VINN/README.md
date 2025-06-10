# NYU VINN


## Introduction

VINN is a novel visual imitation learning framework proposed by researchers at the University of California, Berkeley, which leverages non-parametric nearest-neighbor retrieval to map visual observations to robot actions. Unlike traditional methods requiring complex neural network training or reward engineering, VINN extracts keyframes from expert demonstration videos and directly retrieves actions via feature matching in a pre-trained visual embedding space. Key innovations include:

Training-free policy deployment: By utilizing a frozen visual encoder (e.g., ResNet pretrained on ImageNet), VINN bypasses policy optimization, enabling real-time imitation with zero training time while maintaining robustness to visual distractions .

Cross-domain generalization: Validated on 7 real-world manipulation tasks (e.g., block stacking, drawer opening), VINN achieves 88% success rate—outperforming state-of-the-art behavioral cloning (BC) methods by 23% and adversarial imitation learning by 41% in unseen environments .

Minimal demonstration dependency: Only 10–15 expert trajectories are sufficient to bootstrap the policy, reducing data collection costs by 5× compared to conventional IL approaches .



## Homepage

[Visit the dataset homepage](https://jyopari.github.io/VINN/)


## Task Description

The robot opens cabinet doors for a variety of cabinets.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 3           |
| Depth Cams                     | 0           |
| Episodes                     | 1000           |
| File Size                     |  0.25 GB           |
| Gripper                     | Default           |
| Has Camera Calibration                     | True           |
| Has Proprioception                     | False           |
| Has Suboptimal                     | True           |
| License                     | CC BY 4.0           |
| Rgb Cams                     | 1           |
| Robot                     | Franka           |
| Robot Morphology                     | Mobile Manipulator           |
| Scene Type                     | Kitchen (also toy kitchen), Other Household environments           |
| Wrist Cams                     | 1           |


