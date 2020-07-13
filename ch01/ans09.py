import random

def typoglycemia(str):
    ans = []
    for w in str.split():
        if len(w) > 4 :
            mid = list(w[1:-1])
            random.shuffle(mid)
            w = w[0] + "".join(mid) + w[-1]
        ans.append(w)
    return ans

if __name__ == "__main__":
    text = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(text)
    print( " ".join(typoglycemia(text)))
