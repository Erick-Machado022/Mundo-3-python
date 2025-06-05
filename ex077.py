palavra = ('casa', 'hotel', 'programar', 'python', 'computador', 'estudar', 'futuro', 'mercado', 'loja', 'papelaria')
print('=-='*15)
print(f'{"Contador de vogais":^45}')
print('=-='*15)
for p in palavra:
    print(f'\nA palavra {p} tem as vogais:', end='')
    for letra in p:
        if letra in 'aeiou':
            print(f'{letra}',end=' ')