import pandas as pd
import re
import requests

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
            v3 = remove_markdown(v2)
            items[m.group(1)] = v3

    return items

def remove_emphasis(text):
    pattern_emphasis = r'\'{2,5}'
    return re.sub(pattern_emphasis, '', text)

def remove_inner_link(text):
    pattern_link = r'\[\[(?:[^:\]]+?\|)?([^:]+?)\]\]'
    return re.sub(pattern_link  , r'\1', text)

def remove_markdown(text):
    pattern_mk = r'<[br|ref][^>]*?>.+?<\/[br|ref][^>]*?>|<br \/>|<ref>'
    return re.sub(pattern_mk, '', text)

def get_url(text):
    url_file = text['国旗画像'].replace(' ', '_')
    url = 'https://commons.wikimedia.org/w/api.php?action=query&titles=File:' + url_file + '&prop=imageinfo&iiprop=url&format=json'
    data = requests.get(url)
    return re.search(r'"url":"(.+?)"' ,data.text).group(1)

if __name__ == "__main__":
    file = './ch03/jawiki-country.json'
    f_items = custom_filter(file)
    print(get_url(f_items))
