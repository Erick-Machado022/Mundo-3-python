lista = [] 
soma = media = 0
while True:
    cadastro = {}
    cadastro['nome'] = input('Nome:')
    cadastro['sexo'] = input('Sexo: [F/M] ').strip().upper()[0]
    if cadastro['sexo'] not in 'FM':
        while True:
            cadastro['sexo'] = input('Erro, só aceitamos (F) para feminino ou (M) para masculino: ').strip().upper()[0]
            if cadastro['sexo'] in 'FM':
                break
    cadastro['idade'] = int(input('Idade: '))
    soma += cadastro['idade']
    
    lista.append(cadastro.copy())
    opc = input('Quer continuar? [S/N]').strip().upper()[0]
    if opc not in 'SN':
        while True:
            opc = input('Erro, só aceitamos (S) para sim ou (N) para não: ').strip().upper()[0]
            if opc in 'SN':
                break
    if opc == 'N':
        break
print(lista)
print('-='*30)
print(f'Temos o total de {len(lista)} pessoas cadastradas.')
media = soma / len(lista)
print(f'A média de idades são {media:.2f}')
print('As mulheres cadastradas foram: ',end='')
for p in lista:
    if p['sexo'] in 'F':
        print(f'{p["nome"]}', end=' ')
print()
print('Pessoas mais velhas que a média de idade:')
for m in lista:
    if m['idade'] > media:
        print(f'{m["nome"]}, idade {m["idade"]}.', end=' ')


