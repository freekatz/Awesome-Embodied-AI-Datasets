# RECON


## Introduction

RECON is a novel open-world robotic navigation framework that enables rapid discovery and reliable navigation to user-specified visual goals in unseen environments. Its core innovation lies in integrating latent goal-conditioned models with topological memory graphs, allowing robots to generalize exploration strategies across diverse scenes without pre-built maps. The framework operates in three phases:

Prior Experience Training:

Trains a goal-conditioned distance and action prediction model using historical interaction data from previously visited environments.

Employs step count as a distance proxy and hindsight relabeling to generate supervision signals, learning robust spatial relationships between observations and actions.

New Environment Exploration:

Combines frontier-based exploration (identifying unknown regions) with latent goal sampling (predicting high-reward targets via the learned model).

Continuously fine-tunes the model with real-time interactions to adapt to environmental dynamics (e.g., lighting changes, movable obstacles).

Navigating Explored Environments:

Represents the environment as a sparse topological graph G, where nodes are key locations and edges encode traversability costs.

Plans subgoal paths through G using the fine-tuned model, enabling efficient long-horizon navigation to user-defined targets (e.g., "find a red chair") with 92% success rate in cluttered indoor scenes.



## Homepage

[Visit the dataset homepage](https://sites.google.com/view/recon-robot)


## Task Description

Mobile robot explores outdoor environments using a scripted policy


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF velocity           |
| Control Frequency                     | 3           |
| Depth Cams                     | 1           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | False           |
| Has Suboptimal                     | True           |
| Rgb Cams                     | 2           |
| Robot Morphology                     | Wheeled Robot           |
| Scene Type                     | Outdoors           |
| Wrist Cams                     | 1           |


