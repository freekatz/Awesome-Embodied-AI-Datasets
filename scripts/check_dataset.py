import argparse
import sys
from pathlib import Path

import yaml

NULL = 'null'

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

def check_info(dataset_info):
    with open(dataset_info, "r") as f:
        info = yaml.safe_load(f)
    print(info)
    info_must, info_valid = [], []
    must_keys = ['license', 'url', 'short_description', 'task_description']
    for k in must_keys:
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
        'check_root': dataset_root.parent.name == 'datasets',
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
