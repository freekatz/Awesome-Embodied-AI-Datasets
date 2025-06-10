# Saytap


## Introduction

SayTap is a novel framework that bridges natural language commands with low-level quadrupedal locomotion control by using foot contact patterns as a universal interface. Developed by researchers at UC Berkeley and Google DeepMind, it allows users to flexibly dictate diverse robotic gaits (e.g., "trot slowly backward" or "jump over obstacles") without manual trajectory engineering. Key innovations include:

Language-to-Contact Translator:

Leverages large language models (LLMs) to convert free-form instructions into temporal foot contact patterns (binary sequences indicating ground contact for each leg).

Achieves >50% accuracy in predicting optimal contact patterns for 30+ tasks, outperforming motion-scripted baselines by 2.1× .

Contact-Conditioned Controller:

Uses reinforcement learning to map contact patterns to joint angles and motor torques, with reward functions prioritizing stability and energy efficiency.

Supports zero-shot transfer to real robots (Unitree Go1, A1) with 87% task success in unstructured environments .

Feasible Distribution Exposure:

Novel method to expose controllers to dynamically feasible contact distributions, enabling robust adaptation to terrain perturbations and slippery surfaces .



## Homepage

[Visit the dataset homepage](https://saytap.github.io/)


## Task Description

A Unitree Go1 robot follows human command in natural language (e.g., "trot forward slowly")


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | Joint position           |
| Control Frequency                     | 50           |
| Depth Cams                     | 0           |
| Episodes                     | 256           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| Language Annotations                     | Natural           |
| License                     | CC BY 4.0           |
| Rgb Cams                     | 0           |
| Robot                     | PAMY2           |
| Robot Morphology                     | Quadrupedal Robot           |
| Scene Type                     | Indoor, on a flat floor           |
| Wrist Cams                     | 0           |


