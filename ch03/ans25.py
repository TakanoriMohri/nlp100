import pandas as pd
import re

def custom_filter(json_file_path):
    title_uk = 'title=="イギリス"'
    pattern = re.compile(r'^\|(.+?)\s+=\s*(.+)$')
    df = pd.read_json(file, lines=True)
    lines = df.query(title_uk)['text'].values[0].split('\n')

    items = {}
    for line in lines:
        m = re.search(pattern, line)
        if m is not None:
            items[m.group(1)] = m.group(2)

    return items

if __name__ == "__main__":
    file = './ch03/jawiki-country.json'
    f_items = custom_filter(file)
    for k, v in f_items.items():
        print(k + ' : ' + v)
