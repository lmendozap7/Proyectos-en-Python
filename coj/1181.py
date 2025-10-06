while True:
    numero = int(raw_input())
    if numero == -1:
        break
    else:
        fib = [0] * 50
        fib[0] = 0;
        fib[1] = 1;
        for i in range(2, 50):
            fib[i] = fib[i - 1] + fib[i - 2] + 1
        print fib[numero], fib[numero + 1]
