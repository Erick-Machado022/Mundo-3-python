from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores para a lista: ', end='')
    for cont in range(5):
        num = randint(1,10)
        lista.append(num)
        print(f'{num}', end=' ')
        sleep(.3)
    print()

def SomaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos valores pares de {numeros} resultam em {soma}')
    

numeros = []
sorteia(numeros)
SomaPar(numeros)
