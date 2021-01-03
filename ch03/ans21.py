import pandas as pd

def category_filter(json_file_path):
    title_uk = 'title=="イギリス"'
    df = pd.read_json(file, lines=True)
    uk = df.query(title_uk)['text'].values[0]
    lines = uk.split('\n')
    return list(filter(lambda x: '[Category:' in x, lines))

if __name__ == "__main__":
    file = './ch03/jawiki-country.json'
    ans = category_filter(file)
    for a in ans:
        print(a)
