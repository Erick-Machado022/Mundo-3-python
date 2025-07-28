jogador = {}
partidas = []
jogador['nome'] = input('Nome do Jogador: ')
jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for p in range(jogos):
    partidas.append(int(input(f'   Quantos gols na partida {p+1}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {jogos} partidas.')
for i,v in enumerate(jogador['gols']):
    print(f'Na {i+1}ª partida, marcou {v}')
print(f'O total de gols foi: {jogador["total"]}')