import pandas as pd

def tab2space(file, ansfile):
    df = pd.read_csv(file, sep='\t', header=None)
    df.to_csv(ansfile, sep=' ', header=None, index=False)

if __name__ == "__main__":
    file = './ch02/popular-names.txt'
    ansfile = './ch02/ans11.txt' 
    tab2space(file, ansfile)
