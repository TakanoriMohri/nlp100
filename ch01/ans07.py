def main():
    print(template(12, "気温", 22.4))

def template(x, y, z):
    return f'{x}時の{y}は{z}'
     
if __name__ == "__main__":
    main()