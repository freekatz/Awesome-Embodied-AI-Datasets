# CMU Stretch


## Introduction

VRB (Visual Robotic Bridge) bridges the gap between computer vision models and real-world robotic deployment by learning visual affordances—defining where and how humans interact with objects (e.g., grasping a cup handle or pushing a door)—from internet-scale human interaction videos to serve as structured priors for robot tasks, training an affordance prediction model with egocentric and third-person human videos and integrating it into four key robot learning paradigms (offline imitation learning for translating human demonstrations into robot actions via affordance-guided policy training, exploration for identifying interaction hotspots using affordances, goal-conditioned learning for generating trajectories based on object affordances to achieve task objectives, and reinforcement learning action parameterization for optimizing low-level control with affordance-derived action constraints); validated across 4 real-world environments, 10+ diverse tasks (e.g., door opening, tool use), and 2 robotic platforms in unstructured settings, VRB achieves task generalization via cross-category affordance transfer (e.g., mapping "knob-turning" from doors to valves), reduces demonstration requirements by 70% compared to end-to-end methods, maintains >85% success under visual noise and occlusion, with code, models, and datasets available on the Project Website.


## Homepage

[Visit the dataset homepage](https://robo-affordances.github.io/)


## Task Description

Robot interacting with different household environments.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 10           |
| Depth Cams                     | 0           |
| Gripper                     | Default           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| Language Annotations                     | Templated           |
| License                     | MIT           |
| Rgb Cams                     | 1           |
| Robot Morphology                     | Mobile Manipulator           |
| Scene Type                     | Kitchen (also toy kitchen), Other Household environments           |
| Wrist Cams                     | 0           |


