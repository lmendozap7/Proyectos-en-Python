casos = int(raw_input())
for i in range(casos):
    fila, col = map(int, raw_input().split())
    hacer = True
    if col == fila:
        if fila % 2 == 0:
            print('L')
        else:
            print('R')

        hacer = False
    if fila < col and hacer:
        if fila % 2 == 0 and hacer:
            print('L')
            hacer = False

        if fila % 2 == 1 and hacer:
            print('R')
            hacer = False

    if fila > col and hacer:
        if col % 2 == 0 and hacer:
            print('U')
            hacer = False

        if col % 2 == 1 and hacer:
            print('D')