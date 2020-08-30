import pandas as pd

def wc(file):
    df = pd.read_csv(file, sep='\t', header=None)
    print(len(df))

if __name__ == "__main__":
    file = './ch02/popular-names.txt'
    wc(file)