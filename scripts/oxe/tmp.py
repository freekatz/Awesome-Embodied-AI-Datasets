import argparse
from pathlib import Path

import yaml
from openpyxl import load_workbook
import pandas as pd

NULL = 'null'

def read_data(filename):
    excel_file = pd.ExcelFile(filename)
    df = excel_file.parse('Sheet1')

    wb = load_workbook(filename)
    sheet = wb.active
    data_list = []

    for row in list(sheet.rows)[1:]:
        row_data = {}

        for cell in row:
            col_name = df.columns[cell.column - 1]

            if col_name == 'Dataset':
                hyperlink = cell.hyperlink.target if cell.hyperlink else None
                row_data[col_name] = {
                    'text': cell.value,
                    'hyperlink': hyperlink
                }
            else:
                row_data[col_name] = cell.value

        data_list.append(row_data)

    for i, data in enumerate(data_list):
        new_data = {}
        for k, v in data.items():
            if k.find('Unnamed') != -1:
                continue
            if isinstance(v, dict):
                new_data['name'] = v['text']
                new_data['url'] = v['hyperlink']
            else:
                k = k.replace('# ', '')
                k = k.replace(' (GB)', '')
                k = k.lower()
                k = k.replace(' ', '_')
                k = k.replace('?', '')
                if k == 'description':
                    k = 'task_description'
                if k in ['citation', 'latex_reference', 'registered_dataset_name']:
                    continue
                if v == 'Yes':
                    v = True
                elif v == 'No':
                    v = False
                if isinstance(v, str):
                    v = v.strip()
                    v = v.replace('\n', ' ')
                    v = v.replace('None', NULL)
                    v = v.replace('N/A', NULL)
                if v is None:
                    v = NULL
                new_data[k] = v
        data_list[i] = new_data
    return data_list


def generate_folder(folder: Path, dataset: dict):
    dataset_folder = folder / dataset['name'].replace(' ', '_')
    if dataset_folder.exists():
        return
    dataset_folder.mkdir(parents=True, exist_ok=True)

    info_file = dataset_folder / 'info.yaml'
    readme_file = dataset_folder / 'README.md'

    info = {
        'license': NULL,
        'short_description': NULL,
    }
    for k, v in dataset.items():
        info[k] = v
    try:
        with open(info_file, 'w', encoding='utf-8') as file:
            yaml.dump(info, file, allow_unicode=True)
    except Exception as e:
        print(f"write info failed: {e}")

    markdown = f'# {dataset["name"]}\n\n'
    with open(readme_file, 'w', encoding="utf-8") as f:
        f.write(markdown)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--datasets', type=str, default='./datasets', required=False)
    parser.add_argument('--file', type=str, default='./OXE.xlsx', required=False)
    args = parser.parse_args()

    data_list = read_data(args.file)
    datas = []
    for data in data_list:
        # generate_folder(Path(args.datasets), data)
        datas.append({
            'dataset_name': data['name'],
            'url': data['url'],
        })

    print(datas[40:])
