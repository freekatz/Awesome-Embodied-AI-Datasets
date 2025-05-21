import argparse
from pathlib import Path

from common import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--datasets', type=str, default='./datasets', required=False)
    args = parser.parse_args()

    dataset_root = Path(args.datasets)
    example_dataset_root = dataset_root / 'An_Example_Dataset'
    readme_tmpl = example_dataset_root / 'README.md.tmpl'

    dataset_list = list_dir(dataset_root)

    for dir in dataset_list:
        if dir.name.startswith(example_dataset_root.name):
            continue
        target = dir / 'README.md.tmpl'
        if not target.exists():
            shutil.copy(readme_tmpl, target)

        cmd = [
            'python',
            'scripts/render_dataset_readme.py',
            '--dataset',
            str(dir.absolute()),
            '--force',
        ]
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f'updating README.md for {dir}')
        target.unlink()
