import matplotlib.pyplot as plt
import japanize_matplotlib
from collections import defaultdict

def parse_mecab(block):
    res = []
    for line in block.split('\n'):
        if line =='':
            return res
        (surface, attrs) = line.split('\t')
        attr = attrs.split(',')
        data ={
            'surface':surface,
            'base':attr[6],
            'pos':attr[0],
            'pos1':attr[1]
        }
        if data['pos'] == '記号':
            continue
        res.append(data)

def generate_dictonary(blocks):
    dic = defaultdict(int)
    for block in blocks:
        for text in block:            
            dic[text['surface']] += 1
    return dic

if __name__ == "__main__":
    file = './ch04/neko.txt.mecab'
    with open(file, mode='r', encoding='utf-8') as f:
        text = f.read().split('EOS\n')
    blocks = list(filter(lambda x: x != '', text))
    blocks = [parse_mecab(block) for block in blocks]
    dic = generate_dictonary(blocks)

    data = dic.values()
    plt.figure(figsize=(8, 4))
    plt.hist(data, bins=100)
    plt.savefig('./ch04/ans38.png')


