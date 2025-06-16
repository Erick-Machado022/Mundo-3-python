lista = []
lista_par = []
lista_impar = []
while True:
    num = int(input('Digite um número: '))
    if num not in lista:
            lista.append(num)
            if num %2 == 0:
                lista_par.append(num)
            elif num %2 == 1:
                lista_impar.append(num)
    else:
        print('número já adicionado na lista.') 
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
print('-='*40)
print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {lista_par}')
print(f'A lista de ímpares é: {lista_impar}')

    