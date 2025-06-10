'''
Crie um programa onde o usuário possa digitar vários valores numéricos e 
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será 
adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.'''

lista = []
while True:
    n = int(input('Digite um valor:'))
    
    if n not in lista:
        lista.append(n)
        print('Valor Adicionado com sucesso...')
    else:
        print('Valor duplicado não vou adicionar na lista.')
    while True:
        cont = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if cont in 'SN':
            break
        print('opção invalida. Tente novamente')
    if cont == 'N':
        break
lista.sort()
print(f'Você adicionou os valores {lista}')
        