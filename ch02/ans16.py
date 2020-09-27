import sys
import pandas as pd

if __name__ == "__main__":
    file = './ch02/popular-names.txt'
    if len(sys.argv) == 1:
        print('Set arg n, "python ch02/ans16.py 5"')
    else:
        n = int(sys.argv[1])
        if n < 1:
            print('arg n is more tha 0.')
        else:            
            df = pd.read_csv(file, sep='\t', header=None)
            nrow = -( -len(df) // n)
            for i in range(n):
                df.loc[nrow * i:nrow * (i + 1)].to_csv(f'./ch02/ans16-{i}.txt', sep="\t", header=None, index=False)

