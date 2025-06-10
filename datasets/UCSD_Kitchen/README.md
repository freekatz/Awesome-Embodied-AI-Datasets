# UCSD Kitchen


## Introduction

The UCSD Kitchen Dataset is a real-world multimodal dataset curated by UC San Diego researchers, capturing 150 human demonstrations of daily kitchen activities across 3 distinct home environments. Each demonstration features complex object manipulation tasks (e.g., opening containers, operating appliances) performed by humans under natural conditions. Converted to the RLDS (Reinforcement Learning Datasets) format, it provides:

Task Diversity: 5 core tasks per kitchen environment (e.g., open jar → pour liquid → operate microwave), each with 10 expert trajectories totaling 15 hours of interaction data .

Multimodal Synchronization: Aligned RGB videos (640×480 @30Hz), proprioceptive states, action sequences, and natural language annotations stored in standardized step → episode hierarchies .

Real-World Complexity: Includes challenging scenarios like handling deformable packaging, dealing with liquid spills, and adapting to cluttered countertops .

This dataset serves as a benchmark for robotic imitation learning and human activity understanding, enabling training of robust manipulation policies that achieve 85% success in kitchen assistance tasks when fine-tuned with RLDS-compatible frameworks .



## Homepage

[Visit the dataset homepage](https://www.tensorflow.org/datasets/catalog/ucsd_kitchen_dataset_converted_externally_to_rlds)


## Task Description

The dataset offers a comprehensive set of real-world robotic interactions, involving natural language instructions and complex manipulations with kitchen objects.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 2           |
| Depth Cams                     | 0           |
| Episodes                     | 100           |
| File Size                     |  1.65 GB           |
| Gripper                     | Default           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| Language Annotations                     | Natural           |
| License                     | CC BY 4.0           |
| Rgb Cams                     | 1           |
| Robot                     | DLR SARA           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Kitchen (also toy kitchen)           |
| Wrist Cams                     | 0           |


