import random
from time import sleep
from operator import itemgetter
jogo = {
    'jogador1': random.randint(1,6), 
    'jogador2': random.randint(1,6), 
    'jogador3': random.randint(1,6), 
    'jogador4': random.randint(1,6),}

print('Valores sorteado:')
ranking = []
for k,v in jogo.items(): 
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)

for i,v in enumerate(ranking,start=1 ):
    print(f'{i}º lugar: {v[0]} com {v[1]} pontos ')