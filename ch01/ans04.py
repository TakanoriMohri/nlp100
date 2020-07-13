def main():
    text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    text = text.replace(".", "")
    atoms = [w for w in text.split()]
    idx = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    mp = {}
    for i, atom in enumerate(atoms):
        if (i+1) in idx:
            mp[atom[:1]] = i + 1
        else:
            mp[atom[:2]] = i + 1
    print(mp)

if __name__ == "__main__":
    main()