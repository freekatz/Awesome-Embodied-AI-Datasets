import datetime
import shutil
import subprocess
from os import PathLike
from pathlib import Path
from typing import Optional, Dict, List

import yaml


def git_first_released_date(file_path: PathLike) -> Optional[datetime.datetime]:
    try:
        cmd_commit = [
            'git',
            'rev-list',
            '--max-parents=1',
            'HEAD',
            file_path
        ]
        result_commit = subprocess.run(cmd_commit, capture_output=True, text=True, check=True)
        first_commit_hash = result_commit.stdout.strip().split('\n')[-1]

        if not first_commit_hash:
            print(f"commit not found error.")
            return None

        cmd_date = [
            'git',
            'show',
            '-s',
            '--format=%ci',
            first_commit_hash
        ]
        result_date = subprocess.run(cmd_date, capture_output=True, text=True, check=True)
        commit_date_str = result_date.stdout.strip()

        commit_date = datetime.datetime.strptime(commit_date_str[:19], '%Y-%m-%d %H:%M:%S')
        return commit_date

    except subprocess.CalledProcessError as e:
        print(f"warning: exec git cmd failed: {e.stderr}")
        return None
    except ValueError as e:
        print(f"parse date failed: {e}")
        return None


def load_yaml_file(file_path: PathLike) -> Optional[Dict]:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
            return data
    except Exception as e:
        print(f'load meta info failed: {e}')
        return None

def list_dir(dir: PathLike) -> List[Path]:
    if not isinstance(dir, Path):
        dir = Path(dir)
    dirs = []
    if dir.exists() and dir.is_dir():
        for item in dir.iterdir():
            if item.is_dir():
                dirs.append(item)
    return dirs


def move_file(src: PathLike, dst: PathLike):
    shutil.move(src, dst)


def remove_file(file_path: PathLike):
    file_path = Path(file_path)
    file_path.unlink()
