import sys
import pandas as pd

if __name__ == "__main__":
    file = './ch02/popular-names.txt'
    if len(sys.argv) == 1:
        print('Set arg n, "python ch02/ans14.py 5"')
    else:
        n = int(sys.argv[1])
        if n < 1:
            print('arg n is more tha 0.')
        else:
            df = pd.read_csv(file, sep='\t', header=None)
            print(df.head(n))
