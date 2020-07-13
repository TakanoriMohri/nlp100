def main():
    text1 = "paraparaparadise"
    text2 = "paragraph"
    X = set(ngram(text1, 2))
    Y = set(ngram(text2, 2))

    print(X | Y)
    print(X & Y)
    print(X - Y)

    print('se' in X)
    print('se' in Y)


def ngram(sentence, n):
   return [sentence[i:i+n] for i in range(len(sentence) - n + 1)]

if __name__ == "__main__":
    main()