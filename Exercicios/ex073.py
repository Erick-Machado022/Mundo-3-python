'''
Tabela do dia 03/06/2025
Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros 
colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem 
de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time do Internacional.
'''

tabela = ('Flamengo','Cruzeiro','Bragantino', 'Palmeiras', 'Fluminense', 
          'Bahia','Mirassol', 'Atlético-MG', 'Botafogo', 'Ceará SC',
           'Corinthians', 'Grêmio','São Paulo', 'Internacional', 'Vasco da Gama',
            'EC Vitória', 'Fortaleza', 'Santos', 'Juventude', 'Sport Recife' )
print(f'Os 5 primeiros times do brasileirão são {tabela[0:5]}')
print('-'*20)
print(f'Os Ultimos colocados são os {tabela[-4:]}')
print('-'*20)
print(f'Os times em Ordem alfabética fica {sorted(tabela)}')
print('-'*20)
print(f'O time do Internacional está em {tabela.index("Internacional")+1}º posição')
