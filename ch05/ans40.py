class Morph:
    def __init__(self, morph):
        self.surface, attr = morph.split('\t')
        attr = attr.split(',')
        self.base = attr[6]
        self.pos = attr[0]
        self.pos1 = attr[1]
    def show(self):
        print(self.surface, self.base, self.pos, self.pos1)

def parse_cabocha(block):
    res = []
    for line in block.split('\n'):
        if line == '':
            return res
        elif line[0] == '*':
            continue
        res.append(Morph(line))

if __name__ == "__main__":
    file = './ch05/ai.ja.txt.parsed'
    with open(file, mode='r', encoding='utf-8') as f:
        blocks = f.read().split('EOS\n')
    blocks = list(filter(lambda x: x != '', blocks))
    blocks =[parse_cabocha(block) for block in blocks]
    for m in blocks[1]:
        m.show()