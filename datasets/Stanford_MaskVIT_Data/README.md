# Stanford MaskVIT Data


## Introduction

MaskViT is a novel video prediction framework that leverages masked visual modeling to achieve high-fidelity, long-horizon video generation with minimal domain knowledge. Proposed by researchers at UC Berkeley and Google Research, it extends the masked autoencoding paradigm to spatiotemporal domains, enabling efficient prediction of future frames from partial visual contexts. Key innovations include:

Iterative Decoding with Masked Modeling:

Predicts future frames by iteratively reconstructing masked patches in latent space, reducing computational costs by 512× compared to autoregressive models while maintaining 256×256 resolution .

Parameter-Efficient Architecture:

Combines ViT-based encoders with lightweight convolutional decoders, achieving state-of-the-art prediction quality on BAIR Robot Pushing with 48% fewer parameters than prior work (e.g., DVD-GAN) .

Robotics Integration:

Deployed on real robots for action-conditioned video prediction (e.g., forecasting object trajectories during manipulation), accelerating inference to 22ms/frame (Jetson AGX) and improving MPC planning efficiency by 3.1× .



## Homepage

[Visit the dataset homepage](https://arxiv.org/abs/2206.11894)


## Task Description

The robot randomly pushes and picks objects in a bin, which include stuffed toys, plastic cups and toys, etc, and are periodically shuffled.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | null, actions are run until robot comes to rest near the target position (quasistatic assumption)           |
| Depth Cams                     | 0           |
| Episodes                     | 7328           |
| File Size                     |  1.39 GB           |
| Gripper                     | 3D printed grippper from https://github.com/robertocalandra/sawyer-printable           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | True           |
| Rgb Cams                     | 1           |
| Robot                     | RC Car           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 0           |


