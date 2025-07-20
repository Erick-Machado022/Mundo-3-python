matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite os valores para [{linha}, {coluna}]: '))
        if matriz[linha][coluna] %2 ==0:
            soma_pares += matriz[linha][coluna]
print('=-' * 30)
for linha in range(0,3):
    for coluna in range(0,3):
        
        print(f'[{matriz[linha] [coluna]:^5}]', end='')
    print()
print(f'Os números pares da matriz são {soma_pares}')
soma = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma dos valores da terceira coluna são {soma}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')
