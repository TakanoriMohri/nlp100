def cipher(str):
    ans = ""
    for w in str[::]:
        if ord("a") <= ord(w) <= ord("z"):
            ans += chr(219 - ord(w))
        else:
            ans += w
    return ans

if __name__ == "__main__":
    message = "this is a message."
    print(cipher(message))
    print(message)
