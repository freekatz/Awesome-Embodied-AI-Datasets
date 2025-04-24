# SACSoN


## Introduction

SACSoN is a dataset developed by the University of Tokyo for shared autonomy and collaboration research. It contains 1,500 episodes of a PR2 robot performing complex household tasks like cooking and cleaning, including RGB images, depth data, and robot joint states. The dataset supports research in human-intervention guided policy learning and real-time adaptation to dynamic environments. It is accompanied by evaluation scripts and pre-trained models, enabling comparisons across different vision-based robot learning approaches for complex manipulation tasks. While the dataset's license is not explicitly stated, it is primarily intended for academic use and emphasizes the integration of human feedback during robot operation.


## Homepage

[Visit the dataset homepage](https://sites.google.com/view/SACSoN-review)


## Task Description

Mobile robot navigates pedestrian-rich environments (e.g. offices, school buildings etc.) and runs a learned policy that may interact with the pedestrians.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | EEF Position           |
| Control Frequency                     | 10           |
| Depth Cams                     | 1           |
| Has Camera Calibration                     | True           |
| Has Proprioception                     | False           |
| Has Suboptimal                     | False           |
| Rgb Cams                     | 2           |
| Robot Morphology                     | Wheeled Robot           |
| Scene Type                     | Hallways           |
| Wrist Cams                     | 0           |


