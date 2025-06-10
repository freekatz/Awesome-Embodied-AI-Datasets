# USC Jaco Play


## Introduction

The CLVR Jaco Play Dataset is a multimodal robotic interaction dataset curated by researchers at the University of Southern California (USC) and KAIST. It comprises 1,085 teleoperated trajectories collected via Kinova Jaco 2 manipulators in tabletop environments, covering tasks such as object grasping, stacking, and obstacle avoidance. Key features include:

Multiview Vision: Synchronized RGB streams from third-person (front_cam_ob) and wrist-mounted (mount_cam_ob) cameras;

Robot States: End-effector Cartesian poses (ee_cartesian_pos_ob), velocities (ee_cartesian_vel_ob), and joint positions (joint_pos_ob);

Action Annotations: 3D displacement increments + gripper commands ({0: open, 1: hold, 2: close});

Language Goals: Natural language task descriptions (e.g., "stack the red block on the blue block");

Reward Signals: Binary success labels per trajectory .

Sampled at 10Hz, this dataset enables training of language-conditioned policies and imitation learning algorithms for long-horizon manipulation tasks under open-vocabulary instructions.



## Homepage

[Visit the dataset homepage](https://github.com/clvrai/clvr_jaco_play_dataset)


## Task Description

The robot performs pick-place tasks in a tabletop toy kitchen environment. Some examples of the task include, "Pick up the orange fruit.", "Put the black bowl in the sink."


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 10           |
| Depth Cams                     | 0           |
| Episodes                     | 250           |
| File Size                     |  18.85 GB           |
| Gripper                     | Default           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| Language Annotations                     | Templated           |
| Rgb Cams                     | 2           |
| Robot                     | Franka           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top, Kitchen (also toy kitchen)           |
| Wrist Cams                     | 1           |


