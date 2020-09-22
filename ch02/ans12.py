import pandas as pd

def print_column(number, file, result_file):
    df = pd.read_csv(file, sep='\t', header=None)
    df[number].to_csv(result_file, header=None, index=False)

if __name__ == "__main__":
    file = './ch02/popular-names.txt'
    result_file1 = './ch02/col1.txt' 
    result_file2 = './ch02/col2.txt' 
    print_column(0, file, result_file1)
    print_column(1, file, result_file2)
