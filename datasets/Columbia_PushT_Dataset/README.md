# Columbia PushT Dataset


## Introduction

The Diffusion Policy dataset is a comprehensive collection of robotic manipulation trajectories designed to advance visuomotor policy learning via conditional denoising diffusion models, supporting training and evaluation across 15 diverse tasks from four real-world benchmarks including the Push-T task where a robot must precisely push a T-shaped block into a target zone while navigating the end-effector to a termination area, exemplifying the dataset’s focus on high-precision manipulation under multimodal action distributions and dynamic environmental constraints; its core technical contributions include an action diffusion formulation that reformulates robot actions as a denoising process to iteratively refine noise into optimal actions via stochastic Langevin dynamics for handling multimodal action spaces and high-dimensional sequences, closed-loop action sequences enabling training of policies to predict temporally consistent action sequences (e.g., 10-timestep pushing trajectories) with receding horizon control for balancing long-horizon planning and real-time reactivity in tasks like Push-T requiring mid-execution corrections for object slippage, efficient visual conditioning processing visual observations (e.g., T-block camera feeds) once per inference as conditional inputs to reduce compute latency by >40% for real-time 10 Hz control on physical robots, and architecture flexibility supporting CNN-based (low-frequency tasks) and Transformer-based (high-frequency velocity control) diffusion backbones across tasks from rigid object insertion to deformable fabric manipulation, with performance highlights including a 46.9% average improvement over prior methods (implicit policies, behavior cloning) across 15 tasks, 93% success rate on Push-T under visual occlusion and variable friction forces, and 3× faster convergence than RL baselines using only 200 demonstrations per task.


## Homepage

[Visit the dataset homepage](https://github.com/columbia-ai-robotics/diffusion_policy)


## Task Description

The robot pushes a T-shaped block into a fixed goal pose, and then move to an fixed exit zone.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 10           |
| Depth Cams                     | 0           |
| Episodes                     | 70           |
| File Size                     |  0.14 GB           |
| Gripper                     | 3D printed stick           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| License                     | MIT           |
| Rgb Cams                     | 5           |
| Robot                     | xArm Bimanual           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 1           |


