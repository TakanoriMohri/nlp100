
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
    word = []
    for i in range(0, len(block)):
        if block[i]['pos'] == '名詞':
            word.append(block[i]['surface'])
        else:
            if len(word) > 1:
                phrase.append(''.join(word))
            word = []
    if len(word) > 1:
        phrase.append(''.join(word))
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


