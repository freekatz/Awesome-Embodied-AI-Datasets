
# Contributing to the Dataset Repository

Thank you for your interest in contributing to this project👋. 
We welcome you all to! 

---
## Contribution steps

1. **Fork the Repository**: Click the "Fork" button in the top-right corner to fork this repository to your GitHub account.
2. **Create a Branch**: Clone your forked repository locally and create a new branch:
   ```bash
   git checkout -b add-new-dataset
   ```
3. **Add the Dataset**: Create the dataset directory and fill in the `info.yaml` and `README.md` files 
according to the templates below. Except these, you can also add some other files realted to your databse, 
but please make sure to add the `info.yaml` and `README.md` files.
4. **Commit Changes**: Commit your changes to the branch:
   ```bash
   git add .
   git commit -m "Add new dataset: <Dataset Name>"
   git push origin add-new-dataset
   ```
5. **Create a Pull Request**: Open your forked repository on GitHub, click "Compare & pull request," and submit your changes.
6. **Wait for Review**: The project maintainers will review your pull request and may request changes.
7. **Merge the Pull Request**: Once approved, the maintainers will merge your changes into the main branch. Congratulations! You have successfully contributed to the project.

## Example Dataset Directory Template

Each dataset should follow the directory structure below:

```
datasets/
└── Example_Dataset/
    ├── info.yaml
    └── README.md
```

### `info.yaml` File Template
You can see the example of `info.yaml` file below or refer to the `info.yaml` file of other datasets in the repository.
```yaml
action_space: <string> # Required, robot action space, e.g., "EEF Position"
control_frequency: <integer> # Required, control frequency (Hz), e.g., 20
data_collect_method: <string> # Required, data collection method, e.g., "Human Spacemouse"
depth_cams: <integer> # Required, number of depth cameras, e.g., 0
episodes: <integer> # Required, number of task episodes in the dataset, e.g., 64
file_size: <float> # Required, dataset file size (GB), e.g., 0.35
gripper: <string> # Required, gripper type, e.g., "Default"
has_camera_calibration: <boolean> # Required, whether camera calibration data is included, e.g., true or false
has_proprioception: <boolean> # Required, whether robot proprioception data is included, e.g., true or false
has_suboptimal: <boolean> # Required, whether suboptimal data is included, e.g., true or false
language_annotations: <string> # Required, type of language annotations, e.g., "Templated" or "null"
license: <string> # Required, dataset license, e.g., "MIT" or "null"
name: <string> # Required, dataset name, e.g., "Example Dataset"
rgb_cams: <integer> # Required, number of RGB cameras, e.g., 2
robot: <string> # Required, robot model, e.g., "PR2"
robot_morphology: <string> # Required, robot morphology, e.g., "Single Arm"
scene_type: <string> # Required, scene type, e.g., "Table Top"
short_description: <string> # Optional, a short description of the dataset
task_description: <string> # Required, task description, e.g., "The robot performs various household tasks."
url: <string> # Required, dataset homepage URL, e.g., "https://example.com"
wrist_cams: <integer> # Required, number of wrist cameras, e.g., 1
```

## `README.md` File Formatting Requirements

Each dataset's `README.md` file should include the following content:

```markdown
# Example Dataset

## Introduction
Provide a brief background and purpose of the dataset.

## Dataset Details
- **Action Space**: <action_space>
- **Control Frequency**: <control_frequency> Hz
- **Data Collection Method**: <data_collect_method>
- **Number of Depth Cameras**: <depth_cams>
- **Number of Episodes**: <episodes>
- **File Size**: <file_size> GB
- **Gripper Type**: <gripper>
- **Includes Camera Calibration Data**: <has_camera_calibration>
- **Includes Proprioception Data**: <has_proprioception>
- **Includes Suboptimal Data**: <has_suboptimal>
- **Language Annotations**: <language_annotations>
- **License**: <license>
- **Robot Model**: <robot>
- **Robot Morphology**: <robot_morphology>
- **Scene Type**: <scene_type>
- **Number of Wrist Cameras**: <wrist_cams>

## Task Description
<task_description>

## Dataset Homepage
[Visit the dataset homepage](<url>)
```

---

Thank you for your contribution! If you have any questions, feel free to open an issue.