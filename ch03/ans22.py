import pandas as pd
import re

def category_filter(json_file_path):
    title_uk = 'title=="イギリス"'
    pattern = re.compile(r'\[\[Category:(.*?)(?:\|.*)?\]\]')
    df = pd.read_json(file, lines=True)
    text = df.query(title_uk)['text'].values[0]
    return re.findall(pattern, text)

if __name__ == "__main__":
    file = './ch03/jawiki-country.json'
    ans = category_filter(file)
    for a in ans:
        print(a)
