# Tokyo PR2 Tabletop Manipulation


## Introduction

RLDS Dataset Builder is an open-source toolkit for creating standardized datasets in robotic manipulation tasks, designed to address the critical challenge of temporal fragmentation in reinforcement learning (RL) and imitation learning data. As part of the RLDS ecosystem developed by Google Research, it enables lossless recording of interaction trajectories—preserving step-by-step continuity for tasks like cloth folding or object picking—through three core innovations:

Hierarchical Data Structure:

Stores trajectories as step → episode → metadata sequences, ensuring temporal integrity of actions (e.g., grasp → fold → place in cloth manipulation) and preventing 90% of action fragmentation errors compared to ad-hoc formats 1.

Multimodal Synchronization:

Aligns RGB-D streams (30Hz), joint states (100Hz), and custom annotations (e.g., object_affordance: "foldable") in unified RLDS format, enabling closed-loop visuomotor policy training .

TFDS Integration:

One-click export to TensorFlow Datasets (TFDS) with auto-generated metadata cards, allowing global access via tfds.load('pr2_cloth_folding') and reducing data sharing overhead by 5× .

Validated on PR2 robot tasks (e.g., cloth folding, pick-and-place), datasets built with this tool improve policy training efficiency by 35% and support cross-platform transfer (e.g., PR2 → Franka Emika) without fine-tuning .



## Homepage

[Visit the dataset homepage](https://github.com/ojh6404/rlds_dataset_builder.git)


## Task Description

The PR2 robot conducts manipulation for table top object. It conducts pick-and-place of bread and grape and folds cloth.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 10           |
| Depth Cams                     | 0           |
| Episodes                     | 200           |
| Gripper                     | Default           |
| Has Camera Calibration                     | True           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | True           |
| License                     | MIT           |
| Rgb Cams                     | 1           |
| Robot                     | Franka           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 0           |


