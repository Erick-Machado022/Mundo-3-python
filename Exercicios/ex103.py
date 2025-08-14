def ficha(n='<desconhecido>', gol=0):
    print(f'O jogador {n} fez {gol} na temporada')

#programa principal
print('_'*20)
nome = input('Nome do jogador: ')
g = input('Número de gols: ')
if g.isnumeric():
    g = int(g)
else:
    g=0
if nome.strip() == '':
    ficha(gol=g)
else:
    ficha(nome,g)