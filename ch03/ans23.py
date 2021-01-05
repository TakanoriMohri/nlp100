import pandas as pd
import re

def custom_filter(json_file_path):
    title_uk = 'title=="イギリス"'
    pattern = re.compile(r'^(\=+)\s*([^=]+)\s*(\=+)$')
    df = pd.read_json(file, lines=True)
    lines = df.query(title_uk)['text'].values[0].split('\n')

    section_list = []
    for line in lines:
        m = re.search(pattern, line)
        if m is not None:
            count = str(len(m.group(1)) - 1)
            section_list.append(m.group(2) + ':' + count)

    return section_list

if __name__ == "__main__":
    file = './ch03/jawiki-country.json'
    items = custom_filter(file)
    for item in items:
        print(item)
