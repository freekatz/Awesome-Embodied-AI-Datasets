# UCSD Pick Place


## Introduction

The Open World Minecraft CORL Dataset (OWM-CORL) is a large-scale, multimodal dataset for embodied AI research, collected within Minecraft's open-world environments. It contains over 2,000 hours of interaction trajectories covering navigation, object manipulation, and open-ended exploration tasks, with synchronized sensor streams (RGB, depth, LiDAR, proprioception) and language instructions. Key innovations include:

Structured Task Hierarchy: Organizes 100+ tasks into 3 tiers—atomic actions (e.g., "mine wood"), compositional goals (e.g., "build a cabin"), and open-vocabulary challenges (e.g., "find rare minerals in caves")—enabling curriculum learning for complex behaviors .

Multi-Agent Data: Combines human demonstrations with RL/IL policy trajectories, capturing adaptive strategies for dynamic obstacles (e.g., avoiding creepers) and environmental stochasticity (e.g., weather effects on terrain) .

Open-World Benchmark: Proposes 7 generalization tests for zero-shot adaptation, such as handling unseen biomes (e.g., "navigate icy tundra") or executing language-instructed tasks (e.g., "craft a diamond pickaxe using only desert resources") .

This dataset bridges the sim-to-real gap by providing high-fidelity physics interactions and scalable task diversity, reducing real-world robot policy training costs by 75% in domains like warehouse automation and search-and-rescue .



## Homepage

[Visit the dataset homepage](https://owmcorl.github.io/)


## Task Description

The robot performs pick and place tasks in table top and kitchen scenes. The dataset contains a variety of visual variations.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF velocity           |
| Control Frequency                     | 3           |
| Depth Cams                     | 0           |
| Episodes                     | 100           |
| File Size                     |  3.09 GB           |
| Gripper                     | Default           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | True           |
| Language Annotations                     | Templated           |
| License                     | CC BY 4.0           |
| Rgb Cams                     | 1           |
| Robot                     | DLR EDAN           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top, Kitchen (also toy kitchen)           |
| Wrist Cams                     | 0           |


