# SPOC


## Introduction

SPoC (Search-based Pseudocode to Code) is a novel dataset and framework for translating human-written pseudocode into executable programs through compiler-guided search. Curated by researchers from the University of California, Berkeley, and Google Research, it contains 18,356 C++ programs paired with pseudocode descriptions and test cases. Key innovations include:

Error-Driven Credit Assignment:

Leverages compiler errors (covering 88.7% of program failures) to locate faulty code segments and prioritize alternative translations for specific pseudocode lines, enabling targeted search refinement .

Discretized Translation Units:

Treats each pseudocode line as an independent translation unit, allowing localized error correction without reprocessing the entire program .

Test-Case Validation:

Uses test cases to verify functional correctness of synthesized programs, ensuring semantic alignment with pseudocode intent .

Under a search budget of 100 programs, SPoC increases synthesis success rates from 25.6% (top-one translation) to 44.7% while reducing redundant exploration by 60% .



## Homepage

[Visit the dataset homepage](https://spoc-robot.github.io/)


## Task Description

The robot navigates in the environment and performs pick and place with open vocabulary descriptions.


## Dataset Details

| Field                            | Value                    |
|:---------------------------------|:-------------------------|
| Action Space                     | Joint position           |
| Control Frequency                     | 10           |
| Depth Cams                     | 2           |
| Gripper                     | Default           |
| Has Camera Calibration                     | True           |
| Has Proprioception                     | True           |
| Has Suboptimal                     | False           |
| Language Annotations                     | Scripted language but augmented with LLMs           |
| License                     | CC BY 4.0           |
| Rgb Cams                     | 2           |
| Robot Morphology                     | Single Arm           |
| Scene Type                     | Kitchen (also toy kitchen), Other Household environments, Hallways, multi room environments           |
| Wrist Cams                     | 2           |


