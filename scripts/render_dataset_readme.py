import argparse
import heapq
import sys

from common import *
from configs import *


def new_key(k):
    ks = k.split('_')
    for i, _k in enumerate(ks):
        ks[i] = _k[:1].upper() + _k[1:]
    k = ' '.join(ks)
    return k


def info_table_markdown(meta_info: Dict) -> str:
    visible_meta_length = []
    visible_meta_info = '''| Field                            | Value                    |
|:---------------------------------|:-------------------------|'''

    for k in meta_info.keys():
        if k == custom_meta_info_key:
            continue
        if k not in visible_meta_info_key_details:
            continue
        v = meta_info[k]
        item = f'\n| {new_key(k)}                     | {v}           |'
        visible_meta_info += item
        visible_meta_length.append(len(item))

    if custom_meta_info_key in meta_info.keys():
        custom_meta_infos = meta_info[custom_meta_info_key]
        if custom_meta_info_key in visible_meta_info_key_details:
            for k in custom_meta_infos.keys():
                v = custom_meta_infos[k]
                item = f'\n| {new_key(k)}                     | {v}           |'
                visible_meta_info += item
                visible_meta_length.append(len(item))

    if sum(visible_meta_length) > 0:
        visible_meta_info += '\n\n'
    else:
        visible_meta_info = ''
    return visible_meta_info


def render_readme(readme_path: PathLike, meta_info: dict) -> str:
    field_value_items = info_table_markdown(meta_info)
    render_config = {
        'name': meta_info['name'],
        'url': meta_info['url'],
        'task_description': meta_info['task_description'],
        'field_value_items': field_value_items,
    }

    with open(readme_path, 'r', encoding='utf-8') as file:
        old_readme = file.read()
        new_readme = old_readme.format(**render_config)
    return new_readme


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset', type=str, default='./dataset/An_Example_Dataset', required=False)
    args = parser.parse_args()

    dataset_root = Path(args.dataset)
    dataset_info = dataset_root / 'info.yaml'
    dataset_readme = dataset_root / 'README.md'
    dataset_readme_tmpl = dataset_root / 'README.md.tmpl'

    meta_info = load_yaml_file(dataset_info)
    new_readme = render_readme(dataset_readme_tmpl, meta_info)

    try:
        remove_file(dataset_readme)
        with open(dataset_readme, 'w', encoding="utf-8") as f:
            f.write(new_readme)
        sys.exit(1)
    except Exception as e:
        print(f'failed to write to {dataset_readme}, error: {e}')
        sys.exit(0)

