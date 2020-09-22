import pandas as pd

def get_column(file):
    return pd.read_csv(file, sep='\t', header=None)

def print_dataframe(df, file):
    df.to_csv(file, sep="\t", header=None, index=False)


if __name__ == "__main__":
    c1 = get_column('./ch02/col1.txt')
    c2 = get_column('./ch02/col2.txt')

    df = pd.concat([c1, c2], axis=1)
    print_dataframe(df, './ch02/ans13.txt')

