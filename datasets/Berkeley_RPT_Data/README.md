# Berkeley RPT Data


## Introduction

Robotic Pretrained Transformer (RPT) is a transformer-based model designed to learn unified sensorimotor representations from multimodal robot data by processing interleaved sequences of camera images, proprioceptive robot states, and past actions through tokenizing them into a joint input stream, randomly masking subsets of these tokens during training, and learning to reconstruct the masked content via a masked autoencoding objective to capture cross-modal dependencies crucial for robotic control like correlating visual inputs with motor actions, validated on real-world manipulation tasks as a foundation for efficient policy adaptation with minimal downstream fine-tuning data, featuring key technical innovations including unified tokenization that encodes heterogeneous inputs into a shared token space for seamless multimodal fusion, masked reconstruction that predicts masked tokens via cross-attention over non-masked context to enhance robustness to partial observations, and efficient transfer where pre-trained representations reduce policy training samples by over 40% in downstream tasks such as object grasping and table organization.


## Homepage

[Visit the dataset homepage](https://arxiv.org/abs/2306.10007)


## Task Description

Picking, stacking, destacking, and bin picking with variations in objects.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | Joint position           |
| Control Frequency                     | 30           |
| Depth Cams                     | 0           |
| Episodes                     | =64*9           |
| File Size                     |  6.68 GB           |
| Gripper                     | Default           |
| Has Camera Calibration                     | False           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| Language Annotations                     | Templated           |
| License                     | CC BY-NC 4.0           |
| Rgb Cams                     | 3           |
| Robot                     | Franka           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Table Top           |
| Wrist Cams                     | 1           |


