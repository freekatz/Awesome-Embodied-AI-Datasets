import argparse
import heapq

from common import *
from configs import *


def info_table_markdown(meta_info: Dict) -> str:
    visible_meta_length = []
    visible_meta_info = ''
    for k in visible_meta_info_key:
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


class DatasetInfo:
    def __init__(self, root: Path):
        self.id = root.name.lower()
        self.name = ' '.join(root.name.split('_'))
        cls_id = self.name[0].lower()
        self.cls_id = cls_id if cls_id.isalpha() else 'others'
        self.cls_name = self.cls_id.upper() if cls_id.isalpha() else '#'
        self.url = f'./{root.parent.name}/{root.name}'

        meta_file = root / 'info.yaml'
        self.meta_info = load_yaml_file(meta_file)
        self.license = self.meta_info['license']
        readme_file = root / 'README.md'
        self.release_date = git_first_released_date(readme_file) if self.name != example_dataset_name else None

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

        meta_info_table_markdown = info_table_markdown(self.meta_info)
        desc = self.meta_info['short_description']
        if desc == NULL or desc == '':
            desc = self.meta_info["task_description"]
        desc = f'Homepage: <a href="{self.meta_info["url"]}" target="_blank">{self.meta_info["url"]}</a>\n\n{desc}\n\n'

        markdown = title + license + meta_info_table_markdown + desc
        return markdown


class DatasetList:
    def __init__(self, root: PathLike):
        self.root = root
        datasets = [DatasetInfo(dir) for dir in list_dir(self.root)]
        datasets_with_cls_name = {}
        dataset_cls_id = {}

        valid_dataset_count = 0
        for dataset in datasets:
            if not dataset.is_valid():
                continue
            if dataset.cls_name in datasets_with_cls_name.keys():
                datasets_with_cls_name[dataset.cls_name].append(dataset)
            else:
                datasets_with_cls_name[dataset.cls_name] = [dataset]
            dataset_cls_id[dataset.cls_name] = dataset.cls_id
            valid_dataset_count += 1

        self.dataset_count = valid_dataset_count

        dataset_cls_name = []
        for cls_name, datasets in datasets_with_cls_name.items():
            datasets_with_cls_name[cls_name] = sorted(datasets, key=sort_key)
            dataset_cls_name.append(cls_name)
        dataset_cls_name = sorted(dataset_cls_name, key=sort_key)

        self.dataset_cls = dataset_cls_id  # cls id
        self.dataset_cls_name = dataset_cls_name  # sorted cls name
        self.datasets_with_cls_name = datasets_with_cls_name # cls name: dataset sorted sublist

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
        for dataset in top_heap:
            dataset: DatasetInfo
            markdown += f'- {dataset.release_date.strftime(date_format)}: [{dataset.name}](#{dataset.id})\n'
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
    repo = project_config['repo']
    content = dataset_list.content_markdown()
    trending = dataset_list.trending_markdown()
    released = dataset_list.released_markdown()
    dataset = dataset_list.markdown()

    now = datetime.datetime.now()
    update_date = now.strftime(date_format)
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

    print(f'finished writing {readme}')
