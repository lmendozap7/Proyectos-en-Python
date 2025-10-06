try:
    while True:
        exponente = long(raw_input())
        print (pow(7, exponente, 9))
except:
    EOFError
    exit()