casos=input()
for i in range(casos):
    inicio, fin,a,d=map(int,raw_input().split(" "))
    contador=0
    fin+=1
    for j in range(inicio, fin):
        if not j % a == 0 and not j % (a + d) == 0 and not j % (a + 2 * d) == 0 and not j % (a + 3 * d) == 0 and not j % (a + 4 * d) == 0:
           contador+=1
    print contador