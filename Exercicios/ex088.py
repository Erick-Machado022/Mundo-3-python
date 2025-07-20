import random
from time import sleep
lista = []
jogos = []
quant = int(input('Quantos jogos vocÇe quer que eu sorteie?'))
total_jogos = 1
while total_jogos <= quant:
    cont = 0
    while True:
        num = random.randint(1,60)
        if num not in lista:
            lista.append(num)
            cont +=1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total_jogos +=1
print('-='*3, f' SORTEANDO {quant} DE JOGOS', '-='*3)
for i, l in enumerate(jogos):
    print(f'Resultado do {i+1}º jogo: {jogos}')