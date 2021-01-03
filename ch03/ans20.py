import pandas as pd

def title_filter(json_file_path):
    title_uk = 'title=="イギリス"'
    df = pd.read_json(file, lines=True)
    uk = df.query(title_uk)['text'].values[0]
    return uk

if __name__ == "__main__":
    file = './ch03/jawiki-country.json'
    ans = title_filter(file)
    print(ans)