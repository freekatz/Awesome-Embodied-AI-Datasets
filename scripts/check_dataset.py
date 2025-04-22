import argparse
import sys
from pathlib import Path

from common import load_yaml_file
from configs import *


def check_info(dataset_info):
    info = load_yaml_file(dataset_info)
    info_must, info_valid = [], []
    for k in must_meta_info_key:
        if k not in info.keys():
            info_must.append(f'{k} is missing')
            break
        if info[k] is None:
            info_must.append(f'{k} is None')
            break
        if info[k] == NULL:
            info_must.append(f'{k} is NULL')
            break

    # check license valid
    if info['license'] not in license_infos.keys():
        info_valid.append(f'license invalid: {info["license"]}')

    return info_must, info_valid

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str, default='./dataset/example', required=False)
    args = parser.parse_args()

    dataset_root = Path(args.dataset)
    dataset_info = dataset_root / 'info.yaml'
    dataset_readme = dataset_root / 'README.md'

    info_must, info_valid = check_info(dataset_info)
    check_list = {
        'check_root_parent': dataset_root.parent.name == 'datasets',
        'check_root_exist': dataset_root.exists(),
        'check_info_exist': dataset_info.exists(),
        'check_readme_exist': dataset_readme.exists(),
        'check_info_must': info_must,
        'check_info_valid': info_valid,
    }

    success_count = 0
    for check, check_result in check_list.items():
        msg = f'{check}: '
        if isinstance(check_result, bool):
            if check_result:
                success_count += 1
                msg += 'success'
            else:
                msg += 'failed'
        elif isinstance(check_result, list):
            if len(check_result) == 0:
                success_count += 1
                msg += 'success'
            else:
                msg += 'failed'
                for res in check_result:
                    msg += f'\n - {res}'
        print(msg)

    if success_count < len(check_list):
        print(f'check failed: {success_count}/{len(check_list)}')
        sys.exit(0)
    else:
        print(f'check passed: {success_count}/{len(check_list)}')
        sys.exit(1)
