while True:
    hijos, hijas = map(int, raw_input().split())
    if hijos == 0 and hijas == 0:
        break
    print(hijos + hijas)