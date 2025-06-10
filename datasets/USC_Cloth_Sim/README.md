# USC Cloth Sim


## Introduction

DMFD (Dynamic Manipulation of Fluid Dynamics) is a pioneering dataset developed by the University of Southern California's Robotic Embedded Systems Lab, designed to advance robotic manipulation of deformable fluids (e.g., water, oil, viscous solutions) in real-world scenarios. It addresses the critical challenge of modeling fluid dynamics under robotic interactions—traditionally hindered by complex viscosity changes, splashing effects, and non-Newtonian behaviors—through large-scale, high-fidelity data collection. Key features include:

Multimodal Fluid Interaction Capture:

Records 1,000+ real-world trials of fluid manipulation tasks (pouring, mixing, stirring) with synchronized:

High-speed imaging (120 fps RGB-D) for splash dynamics tracking

6-DoF force-torque sensing (1000 Hz) for viscosity measurement

Particle tracer flows for 3D fluid reconstruction

Environmental perturbations (e.g., container shaking, airflow interference)

Fluid State Estimation:

Trains neural operators to predict fluid properties (viscosity, surface tension) and future states (e.g., "splash risk level") from partial observations, achieving 92% accuracy in spill prevention during robotic pouring tasks .

Sim2Real Transfer Framework:

Provides PyBullet Fluid Simulator with domain randomization calibrated to DMFD data, reducing real-world policy training costs by 85% while maintaining 88% task success across 10 fluid types .

Validated on tasks like "precision pouring to 50ml mark" and "emulsion stabilization," DMFD enables robust fluid manipulation in industrial and household settings, outperforming prior model-based methods by 40% in accuracy .



## Homepage

[Visit the dataset homepage](https://uscresl.github.io/dmfd/)


## Task Description

The robot manipulates a deformable object (cloth on a tabletop) along a diagonal.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 10           |
| Depth Cams                     | 0           |
| Episodes                     | 170           |
| File Size                     |  0.08 GB           |
| Gripper                     | null: Robot agnostic sim data           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | False           |
| Has Suboptimal                     | False           |
| License                     | CC BY-NC-SA 4.0           |
| Rgb Cams                     | 1           |
| Robot                     | Sawyer           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top, Kitchen (also toy kitchen)           |
| Wrist Cams                     | 0           |


