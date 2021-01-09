
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

def get_noun_phrase(block):
    phrase = []
    for i in range(1, len(block)-1):
        if block[i-1]['pos'] == '名詞' and block[i]['surface'] == 'の' and block[i+1]['pos'] == '名詞':
            phrase.append(block[i-1]['surface'] + block[i]['surface'] + block[i+1]['surface'])
    return phrase

if __name__ == "__main__":
    file = './ch04/neko.txt.mecab'
    with open(file, mode='r', encoding='utf-8') as f:
        text = f.read().split('EOS\n')
    blocks = list(filter(lambda x: x != '', text))
    blocks = [parse_mecab(block) for block in blocks]
    for block in blocks:
        phrases = get_noun_phrase(block)
        for phrase in phrases:
            print(phrase)

