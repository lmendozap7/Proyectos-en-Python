for i in range(int(raw_input())):
    numero = int(raw_input())
    sumatoria = 0
    lista = []
    j = 14
    while j >= 0:
        if sumatoria == numero:
            break
        else:
            if sumatoria + 2 ** j <= numero:
                sumatoria += 2 ** j
                lista.append(str(j))
        j -= 1
    print " ".join(sorted(lista))
