
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
    dic = {}
    for block in blocks:
        for text in block:            
            if text['surface'] in dic.keys():
                dic[text['surface']] += 1
            else:
                dic[text['surface']] = 1
    dic_sorted = sorted(dic.items(), key=lambda x:x[1],reverse=True)
    return dic_sorted

if __name__ == "__main__":
    file = './ch04/neko.txt.mecab'
    with open(file, mode='r', encoding='utf-8') as f:
        text = f.read().split('EOS\n')
    blocks = list(filter(lambda x: x != '', text))
    blocks = [parse_mecab(block) for block in blocks]
    dic = generate_dictonary(blocks)
    print(dic)


