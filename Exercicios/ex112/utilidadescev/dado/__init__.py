def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = input(msg).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f"ERRO \"{entrada}\" é um preço invalido")
        else:
            valido = True
            return float(entrada)