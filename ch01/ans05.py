def main(sentence, n):
   return [sentence[i:i+n] for i in range(len(sentence) - n + 1)]



if __name__ == "__main__":
    text = "I am an NLPer"
    print(main(text, 2))
    print(main(text.split(), 2))