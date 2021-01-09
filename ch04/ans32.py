
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
        res.append(data)

if __name__ == "__main__":
    file = './ch04/neko.txt.mecab'
    with open(file, mode='r', encoding='utf-8') as f:
        text = f.read().split('EOS\n')
    blocks = list(filter(lambda x: x != '', text))
    blocks = [parse_mecab(block) for block in blocks]
    for block in blocks:
        for data in block:
            if data['pos'] == '動詞':
                print(data['base'])

