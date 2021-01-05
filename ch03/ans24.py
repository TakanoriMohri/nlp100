import pandas as pd
import re

def custom_filter(json_file_path):
    title_uk = 'title=="イギリス"'
    pattern = re.compile(r'\[\[ファイル:(.+?)\|')
    df = pd.read_json(file, lines=True)
    lines = df.query(title_uk)['text'].values[0].split('\n')

    section_list = []
    for line in lines:
        m = re.search(pattern, line)
        if m is not None:
            section_list.append(m.group(1))

    return section_list

if __name__ == "__main__":
    file = './ch03/jawiki-country.json'
    items = custom_filter(file)
    for item in items:
        print(item)
