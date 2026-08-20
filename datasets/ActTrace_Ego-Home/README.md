# ActTrace Ego-Home


## Introduction

ActTrace Ego-Home focuses on measurement quality over volume: every stream is measured or independently verified, never merely estimated. v0.2 ships 13 episodes (18.0 minutes, 11 household tasks) with 9 synchronized columns: 1080p60 ultra-wide RGB video, metric LiDAR depth (16-bit millimeters, per-pixel confidence), 100 Hz head IMU, dual-hand 2D keypoints with per-point confidence, metric 3D hand trajectories lifted through in-app-calibrated dual-camera extrinsics plus LiDAR depth, 6-DoF head trajectories (TUM format, 30 Hz, up-to-scale), per-frame camera metadata, a cross-stream clock anchor, and dual-register language annotations (verbatim human narration plus machine-generated imperative instruction, provenance disclosed field-by-field).

Every released head trajectory must survive a cross-examination against the gyroscope (angular-rate correlation, shipping bar r >= 0.97, alignment residual <= 0.03 s); episodes that fail are re-recorded or not released, and the dataset card documents the capture-protocol fix (a slow 5-second look-around at episode start and end) that rescued three initially-failing episodes. Per-episode QC health reports and a LeRobot v2.1 converter are included. Free for research (CC BY-NC 4.0); commercial licensing and custom collection are available.


## Homepage

[Visit the dataset homepage](https://huggingface.co/datasets/ActTrace/acttrace-ego-home)


## Task Description

A human demonstrator wearing a head-mounted iPhone performs real household manipulation tasks in real homes: washing cups and dishes, folding laundry and T-shirts, cutting fruit, beating eggs, boiling and pouring water, unpacking parcels, changing trash bags, and clearing the table after a meal. Every episode ships with verbatim human narration plus a machine-generated imperative instruction (provenance disclosed) and human-confirmed action segments with handedness.


## Dataset Details

- **license**: CC BY-NC 4.0
- **episodes**: 13
- **file_size**: 4.2 GB
- **scene_type**: Real Home
- **data_collect_method**: Human demonstration (head-mounted iPhone, ultra-wide RGB + LiDAR)
- **robot**: null (human egocentric demonstration, no robot embodiment)
- **rgb_cams**: 1
- **depth_cams**: 1
- **wrist_cams**: 0
- **has_camera_calibration**: true
- **has_proprioception**: false
- **has_suboptimal**: false
- **language_annotations**: Natural (verbatim human narration + machine-generated imperative instruction, provenance disclosed)
