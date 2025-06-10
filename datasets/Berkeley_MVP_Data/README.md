# Berkeley MVP Data


## Introduction

This repository offers the official PyTorch implementation for two groundbreaking papers on masked visual pretraining in robot learning—"Masked Visual Pre-training for Motor Control" and "Real-World Robot Learning via Masked Visual Pre-training"—which tackle the critical challenge of obtaining generalizable visual representations from limited task-specific data in vision-based robotics; inspired by the success of masked autoencoders (MAEs) in computer vision, the proposed unified pretraining framework reconstructs masked robot observations (such as RGB images and proprioceptive states) to learn transferable spatiotemporal features that accelerate downstream policy learning for motor control tasks and decrease reliance on large-scale in-domain demonstrations, with core technical components including Masked Robot Modeling (MRM), a self-supervised objective for cross-modal representation learning by reconstructing randomly masked patches from robot camera streams and sensor readings; efficient policy adaptation using pretrained weights to initialize visuomotor policies (PPO/BC), reducing downstream training samples by over 50% while enhancing sim-to-real transfer robustness; and benchmark validation showing state-of-the-art performance on 7 real-world tasks like door opening and pick-and-place, achieving a 63% average success rate improvement over non-pretrained baselines, and the repository includes pretrained vision models (ResNet-18/50, ViT-Base) on robotics datasets such as BridgeData V2, modular PPO and BC training code for policy fine-tuning, and evaluation scripts for simulated and physical deployments.


## Homepage

[Visit the dataset homepage](https://arxiv.org/abs/2203.06173)


## Task Description

Basic motor control tasks (reach, push, pick) on table top and toy environments (toy kitchen, toy fridge).


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | Joint position           |
| Control Frequency                     | 5           |
| Depth Cams                     | 0           |
| Episodes                     | 4200           |
| File Size                     |  720.00 GB           |
| Gripper                     | Default           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| Language Annotations                     | Templated           |
| License                     | CC BY-NC 4.0           |
| Rgb Cams                     | 1           |
| Robot                     | Franka           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top, Kitchen (also toy kitchen)           |
| Wrist Cams                     | 1           |


