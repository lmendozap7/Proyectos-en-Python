raw_input()
personas = list(raw_input())
helados = list(raw_input())
while len(personas) > 0:
    if personas[0] == helados[0]:
        print '0'
        del personas[0]
        del helados[0]
    else:
        guardar = helados.index(personas[0])
        print guardar
        del personas[0]
        del helados[guardar]
