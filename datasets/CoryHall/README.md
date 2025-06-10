# CoryHall


## Introduction

Generalized Computation Graphs (GCG) tackle the critical challenge of enabling robots to learn complex navigation policies with minimal real-world interaction by proposing a unified framework that integrates model-free (value-based) and model-based reinforcement learning paradigms to dynamically interpolate between the two approaches, leveraging model-based sample efficiency and model-free flexibility while addressing limitations of traditional navigation methods (computational intensity, rigid assumptions, failure learning gaps) and learning-based approaches (high sample complexity); core innovations include a unified architecture fusing perception (raw images), value estimation (Q-learning), and dynamics modeling into a computation graph for joint policy and environment prediction optimization, self-supervised training via fully autonomous exploration where failures generate corrective data for iterative policy refinement without human intervention, and sample efficiency achieved by sharing features between value and model networks to reduce sample requirements by >80% compared to vanilla Q-learning; validated in simulation car navigation tasks with 92% success rate (vs. Double Q-learning’s 76%) and 15% shorter trajectories, and on a real-world remote-controlled car that learned cluttered indoor navigation (offices with dynamic obstacles) in <5 hours of autonomous training, achieving 85% success in unseen scenarios, GCG offers a scalable framework for sample-efficient robot learning to enable rapid adaptation to complex environments with limited data, a key step toward practical autonomous systems.


## Homepage

[Visit the dataset homepage](https://arxiv.org/abs/1709.10489)


## Task Description

Small mobile robot navigates hallways in an office building using a learned policy.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF velocity           |
| Control Frequency                     | 5           |
| Depth Cams                     | 0           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | False           |
| Has Suboptimal                     | False           |
| License                     | MIT           |
| Rgb Cams                     | 1           |
| Robot Morphology                     | Wheeled Robot           |
| Scene Type                     | Hallways           |
| Wrist Cams                     | 0           |


