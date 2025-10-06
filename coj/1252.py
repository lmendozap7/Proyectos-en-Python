cambio = raw_input()
while True:
    completo = raw_input()
    if not completo == '#':
        cambio += '\n' + completo
    else:
        cambio = cambio.replace("%", "%25")
        cambio = cambio.replace(" ", "%20")
        cambio = cambio.replace("!", "%21")
        cambio = cambio.replace("$", "%24")
        cambio = cambio.replace("(", "%28")
        cambio = cambio.replace(")", "%29")
        cambio = cambio.replace("*", "%2a")
        print(cambio)
        break
