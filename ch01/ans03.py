def main():
    text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    text = text.replace(",", "").replace(".","")
    ans = [len(w) for w in text.split()]
    print(ans)

if __name__ == "__main__":
    main()