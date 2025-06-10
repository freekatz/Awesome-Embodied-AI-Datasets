# Stanford Kuka Multimodal


## Introduction

The Vision and Touch Dataset is a multimodal robotic interaction dataset developed by researchers at Stanford University, designed to advance self-supervised learning of contact-rich manipulation tasks. It addresses the challenge of combining heterogeneous sensory inputs (vision and touch) for robust control in unstructured environments, where traditional methods struggle due to high-dimensional state spaces and sample inefficiency. Key features include:

Multimodal Synchronization:

Combines RGB images (640×480), tactile readings (6-axis force-torque sensor data over 32ms windows), and proprioceptive states (end-effector positions/velocities) to capture interactions during contact-intensive tasks like peg insertion and object assembly.

Self-Supervised Representation Learning:

Trains a neural network to fuse vision-touch-proprioception inputs into a compact 128-D latent space via contrastive learning, enabling efficient policy training with 40% fewer samples than standard RL methods.

Robustness to Perturbations:

Validated on real-world tasks (e.g., inserting pegs with varying geometries), achieving 92% success under external disturbances (e.g., positional shifts, force noise) and generalizing to unseen object shapes with 85% accuracy.

This dataset pioneers the use of cross-modal alignment for contact-rich robotics, demonstrating that tactile feedback compensates for visual occlusion while visual context guides tactile interpretation—critical for deformable object manipulation and precision assembly.



## Homepage

[Visit the dataset homepage](https://sites.google.com/view/visionandtouch)


## Task Description

The robot learns to insert differently-shaped pegs into differently-shaped holes with low tolerances (~2mm).


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 20           |
| Depth Cams                     | 0           |
| Episodes                     | 82432           |
| File Size                     |  799.91 GB           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | True           |
| License                     | MIT           |
| Rgb Cams                     | 1           |
| Robot                     | Multi-Robot           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 0           |


