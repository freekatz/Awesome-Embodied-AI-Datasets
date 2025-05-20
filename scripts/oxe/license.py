import sys

license_dict = {}
l = sys.argv[1]
with open(l, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for i in range(0, len(lines), 3):
        name = lines[i].strip()
        badge = lines[i + 1].strip()
        url = lines[i + 2].strip()
        license_dict[name] = {
            'url': url,
            'badge': badge
        }

# 格式化输出字典内容
formatted_output = ",\n".join([f"'{name}': {{\n        'url': '{info['url']}',\n        'badge': '{info['badge']}'\n    }}" for name, info in license_dict.items()])
print(formatted_output)