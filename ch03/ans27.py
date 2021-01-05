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
            v1 = remove_emphasis(m.group(2))
            v2 = remove_inner_link(v1)
            items[m.group(1)] = v2

    return items

def remove_emphasis(text):
    pattern_emphasis = r'\'{2,5}'
    return re.sub(pattern_emphasis, '', text)

def remove_inner_link(text):
    pattern_link = r'\[\[(?:[^:\]]+?\|)?([^:]+?)\]\]'
    return re.sub(pattern_link  , r'\1', text)


if __name__ == "__main__":
    file = './ch03/jawiki-country.json'
    f_items = custom_filter(file)
    for k, v in f_items.items():
        print(k + ' : ' + v)
