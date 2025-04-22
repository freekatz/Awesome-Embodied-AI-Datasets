import argparse
import datetime
import heapq
import subprocess
from os import PathLike
from pathlib import Path
from typing import Optional, Dict, List

import yaml

NULL = 'null'
config = {
    'repo': 'freekatz/Awesome-Embodied-AI-Datasets',
}
license_infos = {
    'Apache 2.0': {
        'url': 'https://opensource.org/licenses/Apache-2.0',
        'badge': 'https://img.shields.io/badge/License-Apache_2.0-yellowgreen.svg'
    },
    'Boost 1.0': {
        'url': 'https://www.boost.org/LICENSE_1_0.txt',
        'badge': 'https://img.shields.io/badge/License-Boost_1.0-lightblue.svg'
    },
    'BSD 3': {
        'url': 'https://opensource.org/licenses/BSD-3-Clause',
        'badge': 'https://img.shields.io/badge/License-BSD_3--Clause-orange.svg'
    },
    'BSD 2': {
        'url': 'https://opensource.org/licenses/BSD-2-Clause',
        'badge': 'https://img.shields.io/badge/License-BSD_2--Clause-orange.svg'
    },
    'CC0': {
        'url': 'http://creativecommons.org/publicdomain/zero/1.0/',
        'badge': 'https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg'
    },
    'CC BY 4.0': {
        'url': 'https://creativecommons.org/licenses/by/4.0/',
        'badge': 'https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg'
    },
    'CC BY-SA 4.0': {
        'url': 'https://creativecommons.org/licenses/by-sa/4.0/',
        'badge': 'https://img.shields.io/badge/License-CC_BY--SA_4.0-lightgrey.svg'
    },
    'CC BY-NC 4.0': {
        'url': 'https://creativecommons.org/licenses/by-nc/4.0/',
        'badge': 'https://img.shields.io/badge/License-CC_BY--NC_4.0-lightgrey.svg'
    },
    'CC BY-ND 4.0': {
        'url': 'https://creativecommons.org/licenses/by-nd/4.0/',
        'badge': 'https://img.shields.io/badge/License-CC_BY--ND_4.0-lightgrey.svg'
    },
    'CC BY-NC-SA 4.0': {
        'url': 'https://creativecommons.org/licenses/by-nc-sa/4.0/',
        'badge': 'https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg'
    },
    'CC BY-NC-ND 4.0': {
        'url': 'https://creativecommons.org/licenses/by-nc-nd/4.0/',
        'badge': 'https://img.shields.io/badge/License-CC_BY--NC--ND_4.0-lightgrey.svg'
    },
    'EPL 1.0': {
        'url': 'https://opensource.org/licenses/EPL-1.0',
        'badge': 'https://img.shields.io/badge/License-EPL_1.0-red.svg'
    },
    'GPL v3': {
        'url': 'https://www.gnu.org/licenses/gpl-3.0',
        'badge': 'https://img.shields.io/badge/License-GPLv3-blue.svg'
    },
    'GPL v2': {
        'url': 'https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html',
        'badge': 'https://img.shields.io/badge/License-GPL_v2-blue.svg'
    },
    'AGPL v3': {
        'url': 'https://www.gnu.org/licenses/agpl-3.0',
        'badge': 'https://img.shields.io/badge/License-AGPL_v3-blue.svg'
    },
    'LGPL v3': {
        'url': 'https://www.gnu.org/licenses/lgpl-3.0',
        'badge': 'https://img.shields.io/badge/License-LGPL_v3-blue.svg'
    },
    'FDL v1.3': {
        'url': 'https://www.gnu.org/licenses/fdl-1.3',
        'badge': 'https://img.shields.io/badge/License-FDL_v1.3-blue.svg'
    },
    'Hippocratic 2.1': {
        'url': 'https://firstdonoharm.dev',
        'badge': 'https://img.shields.io/badge/License-Hippocratic_2.1-lightgrey.svg'
    },
    'Hippocratic 3.0': {
        'url': 'https://firstdonoharm.dev',
        'badge': 'https://img.shields.io/badge/License-Hippocratic_3.0-lightgrey.svg'
    },
    'IPL 1.0': {
        'url': 'https://opensource.org/licenses/IPL-1.0',
        'badge': 'https://img.shields.io/badge/License-IPL_1.0-blue.svg'
    },
    'ISC': {
        'url': 'https://opensource.org/licenses/ISC',
        'badge': 'https://img.shields.io/badge/License-ISC-blue.svg'
    },
    'MIT': {
        'url': 'https://opensource.org/licenses/MIT',
        'badge': 'https://img.shields.io/badge/License-MIT-yellow.svg'
    },
    'MPL 2.0': {
        'url': 'https://opensource.org/licenses/MPL-2.0',
        'badge': 'https://img.shields.io/badge/License-MPL_2.0-brightgreen.svg'
    },
    'BY': {
        'url': 'https://opendatacommons.org/licenses/by/',
        'badge': 'https://img.shields.io/badge/License-ODC_BY-brightgreen.svg'
    },
    'ODBL': {
        'url': 'https://opendatacommons.org/licenses/odbl/',
        'badge': 'https://img.shields.io/badge/License-ODbL-brightgreen.svg'
    },
    'PDDL': {
        'url': 'https://opendatacommons.org/licenses/pddl/',
        'badge': 'https://img.shields.io/badge/License-PDDL-brightgreen.svg'
    },
    'Perl': {
        'url': 'https://opensource.org/licenses/Artistic-2.0',
        'badge': 'https://img.shields.io/badge/License-Perl-0298c3.svg'
    },
    'Artistic 2.0': {
        'url': 'https://opensource.org/licenses/Artistic-2.0',
        'badge': 'https://img.shields.io/badge/License-Artistic_2.0-0298c3.svg'
    },
    'OFL 1.1': {
        'url': 'https://opensource.org/licenses/OFL-1.1',
        'badge': 'https://img.shields.io/badge/License-OFL_1.1-lightgreen.svg'
    },
    'Unlicense': {
        'url': 'http://unlicense.org/',
        'badge': 'https://img.shields.io/badge/license-Unlicense-blue.svg'
    },
    'WTFPL': {
        'url': 'http://www.wtfpl.net/about/',
        'badge': 'https://img.shields.io/badge/License-WTFPL-brightgreen.svg'
    },
    'Zlib': {
        'url': 'https://opensource.org/licenses/Zlib',
        'badge': 'https://img.shields.io/badge/License-Zlib-lightgrey.svg'
    },
    NULL: {},
}


def get_released_date(file_path: PathLike) -> Optional[datetime.datetime]:
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


def load_meta_info(file_path: PathLike) -> Optional[Dict]:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
            return data
    except Exception as e:
        print(f'load meta info failed: {e}')
        return None


def get_visible_meta_info(meta_info: Dict) -> str:
    visible_meta_key = []
    visible_meta_length = []
    visible_meta_info = ''
    for k in visible_meta_key:
        if k in meta_info.keys():
            v = meta_info[k]
        else:
            v = ''
        visible_meta_info += f'| {v} '
        visible_meta_length.append(len(v))

    visible_meta_info += '|'
    if sum(visible_meta_length) > 0:
        visible_meta_info += '\n|'
        for l in visible_meta_length:
            visible_meta_info += f' :-: |'
        visible_meta_info += '\n\n'
    else:
        visible_meta_info = ''
    return visible_meta_info


def list_dir(dir: PathLike) -> List[Path]:
    if not isinstance(dir, Path):
        dir = Path(dir)
    dirs = []
    if dir.exists() and dir.is_dir():
        for item in dir.iterdir():
            if item.is_dir():
                dirs.append(item)
    return dirs


def sort_key(item):
    sorted_chars = []
    base = item
    if isinstance(item, DatasetInfo):
        base = item.name
    for char in base:
        if 'a' <= char <= 'z':
            priority = 1
        elif 'A' <= char <= 'Z':
            priority = 2
        elif '0' <= char <= '9':
            priority = 3
        else:
            priority = 4
        sorted_chars.append((priority, char))
    return sorted_chars


class DatasetInfo():
    def __init__(self, root: Path):
        self.id = root.name.lower()
        self.name = ' '.join(root.name.split('_'))
        cls = self.name[0].lower()
        self.cls = cls if cls.isalpha() else 'others'
        self.cls_name = self.cls.upper() if cls.isalpha() else '#'
        self.url = f'./{root.parent.name}/{root.name}'

        meta_file = root / 'info.yaml'
        self.meta_info = load_meta_info(meta_file)
        for k in ['license', 'short_description']:
            assert k in self.meta_info.keys()
        self.license = self.meta_info['license']
        assert self.license in license_infos.keys()

        readme_file = root / 'README.md'
        self.release_date = get_released_date(readme_file)

    def __lt__(self, other):
        return self.release_date < other.release_date

    def is_valid(self) -> bool:
        valid = True
        if self.release_date is None:
            valid = False
        return valid

    def markdown(self) -> str:
        title = f'### <a name="{self.id}" href="{self.url}">{self.name}</a>\n\n'

        if self.license != NULL:
            license_info = license_infos[self.license]
            license = f'[![License: {self.license}]({license_info["badge"]})]({license_info["url"]})\n\n'
        else:
            license = ''

        visible_meta_info = get_visible_meta_info(self.meta_info)
        # desc = self.meta_info['short_description']
        desc = f'Homepage: <a href="{self.meta_info["url"]}" target="_blank">{self.meta_info["url"]}</a>\n\n{self.meta_info["task_description"]}\n\n'

        markdown = title + license + visible_meta_info + desc
        return markdown


class DatasetList():
    def __init__(self, root: PathLike):
        self.root = root
        datasets = [DatasetInfo(dir) for dir in list_dir(self.root)]
        datasets_with_cls_name = {}
        dataset_cls = {}
        for dataset in datasets:
            if not dataset.is_valid():
                continue
            if dataset.cls_name in datasets_with_cls_name.keys():
                datasets_with_cls_name[dataset.cls_name].append(dataset)
            else:
                datasets_with_cls_name[dataset.cls_name] = [dataset]
            dataset_cls[dataset.cls_name] = dataset.cls

        self.dataset_count = len(datasets)

        dataset_cls_name = []
        for cls_name, datasets in datasets_with_cls_name.items():
            datasets_with_cls_name[cls_name] = sorted(datasets, key=sort_key)
            dataset_cls_name.append(cls_name)
        dataset_cls_name = sorted(dataset_cls_name, key=sort_key)

        self.dataset_cls = dataset_cls
        self.dataset_cls_name = dataset_cls_name
        self.datasets_with_cls_name = datasets_with_cls_name

        self.content = {}
        self.trending = {}

        now = datetime.datetime.now()
        two_weeks_ago = now - datetime.timedelta(weeks=2)

        newly_datasets = []
        for cls_name in self.datasets_with_cls_name:
            for dataset in self.datasets_with_cls_name[cls_name]:
                if dataset.release_date >= two_weeks_ago:
                    newly_datasets.append(dataset)
        self.newly_datasets = newly_datasets
        self.newly_released = {}

    def __len__(self) -> int:
        return self.dataset_count

    def content_markdown(self) -> str:
        markdown = ''
        for cls_name in self.dataset_cls_name:
            cls = self.dataset_cls[cls_name]
            markdown += f'- [{cls_name}](#{cls})\n'
        return markdown

    def trending_markdown(self) -> str:
        # todo
        return ''

    def released_markdown(self) -> str:
        topn = 10
        if len(self.newly_datasets) > topn:
            top_heap = self.newly_datasets[:topn]
            heapq.heapify(top_heap)

            for item in self.newly_datasets[topn:]:
                if not item < top_heap[0]:
                    heapq.heapreplace(top_heap, item)
        else:
            top_heap = self.newly_datasets
        top_heap = sorted(top_heap, key=lambda x: x.release_date, reverse=True)

        markdown = ''
        # release_format = "%Y-%m-%d %H:%M:%S"
        release_format = "%Y-%m-%d"
        for dataset in top_heap:
            dataset: DatasetInfo
            markdown += f'- {dataset.release_date.strftime(release_format)}: [{dataset.name}](#{dataset.id})\n'
        return markdown

    def markdown(self) -> str:
        markdown = ''
        for cls_name in self.dataset_cls_name:
            cls = self.dataset_cls[cls_name]
            markdown += f'## <a name="{cls}"></a>{cls_name}\n\n'
            for dataset in self.datasets_with_cls_name[cls_name]:
                markdown += dataset.markdown()
        return markdown


def render_readme(readme_path: PathLike, dataset_list: DatasetList) -> str:
    repo = config['repo']
    content = dataset_list.content_markdown()
    trending = dataset_list.trending_markdown()
    released = dataset_list.released_markdown()
    dataset = dataset_list.markdown()

    now = datetime.datetime.now()
    update_date = now.strftime("%Y-%m-%d")
    render_config = {
        'repo': repo,
        'dataset_count': len(dataset_list),
        'latest_update_date': update_date,
        'content': content,
        'trending': trending,
        'released': released,
        'dataset_list': dataset,
    }

    with open(readme_path, 'r', encoding='utf-8') as file:
        old_readme = file.read()
        new_readme = old_readme.format(**render_config)
    return new_readme


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--datasets', type=str, default='./datasets', required=False)
    parser.add_argument('--readme', type=str, default='./README.md', required=False)
    args = parser.parse_args()

    dataset_root = Path(args.datasets)
    readme = Path(args.readme)
    readme_tmpl = Path(args.readme + '.tmpl')

    dataset_list = DatasetList(dataset_root)
    new_readme = render_readme(readme_tmpl, dataset_list=dataset_list)

    with open(readme, 'w', encoding="utf-8") as f:
        f.write(new_readme)
