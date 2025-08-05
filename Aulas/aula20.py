def soma(* numeros):
    s = 0
    for valor in numeros:
        s += valor
    print(f'A soma dos valores {numeros} resultam em {s}')


soma(8, 3)
soma(7, 5, 1)