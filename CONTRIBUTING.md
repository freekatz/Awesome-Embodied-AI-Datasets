
# Contributing to the Dataset Repository

Thank you for your interest in contributing to this project👋. 
We welcome you all to! 

---

## Example Dataset Directory Template

Each dataset should follow the directory structure below:

```
datasets/
└── Example_Dataset/
    ├── assets (optional, put your pictures)
    ├── examples (optional, put your example codes or data)
    ├── info.yaml
    └── README.md
```

> [!TIP]
> We have provided an example dataset template, see: [An Example Dataset](./datasets/An_Example_Dataset)


---
## Contribution steps

1. **Fork the Repository**: Click the "Fork" button in the top-right corner to fork this repository to your GitHub account.
2. **Create a Branch**: Clone your forked repository locally and create a new branch:
   ```bash
   git switch -c add-new-dataset
   ```
3. **Add the Dataset**: Copy the dataset template directory into `datasets` folder
   - Rename your dataset directory based on the dataset name, please replace blank ` ` with `_`
   - Fill in the required, optional and custom fields in the `info.yaml`
   - Run script to check info: `python scripts/check_dataset.py --dataset <your_dataset_directory>`
   - Run script to render `README.md` automatically: `python ./scripts/render_dataset_readme.py --dataset <your_dataset_directory>`
   - Fill in the **Introduction** section of the `README.md`
   - Delete the template file `README.md.tmpl`
   
   Except these, you can also add some other files relevant to your dataset, such as example codes and data.
4. **Commit Changes**: Commit your changes to the branch:
   ```bash
   git add .
   git commit -m "Add new dataset: <Your Dataset Name>"
   git push --set-upstream origin add-new-dataset
   ```
5. **Create a Pull Request**: Open your forked repository on GitHub, click "Compare & pull request," and submit your changes.
6. **Wait for Review**: The project maintainers will review your pull request and may request changes.
7. **Merge the Pull Request**: Once approved, the maintainers will merge your changes into the main branch. Congratulations! You have successfully contributed to the project.


---
Thank you for your contribution! If you have any questions, feel free to open an issue.
