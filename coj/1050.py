def main():
    contador=0
    numero=int(raw_input())
    for i in range(1,numero+1):
        if mcd(numero,i)==1:
           contador+=1
    print contador

def mcd(a,b):
    if b==0:
       return a
    else:
         return mcd(b,a%b)

if __name__ == '__main__':
    main()
