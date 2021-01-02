import sys
import pandas as pd

if __name__ == "__main__":
    file = './ch02/popular-names.txt'
    df = pd.read_csv(file, sep='\t', header=None)
    newdata = df[0].unique()
    newdata.sort()
    print(newdata)
