'''Crie um programa que vai ler vários números e colocar em uma lista.Depois disso, mostre
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.       
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
cont = 0
while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
        cont += 1
    else:
        print('Número já está dentro da lista.')
        
    print('-'*40)
    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    print('-'*40)
    while continuar not in "SN":
        continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
        print('-'*40)
    if continuar == 'N':
        break
print(f'Os números digitados foram {lista}')
print(f'Foram adicionados {cont} números na lista ')
print(f'Os números digitados em ordem decrescente: {sorted(lista, reverse=True)}')
if 5 in lista:
    print(f'o valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')
