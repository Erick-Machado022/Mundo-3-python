temp = []
princ = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor =temp[1] 
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp in 'Nn':
        break
print('-=' *20)
print(f'Foram cadastradas {len(princ)} pessoas')
print('As pessoas mais pesadas foram: ', end='')
for p in princ:
    if p[1] == maior:
        print(f'{p[0]}', end=', ')
print(f'Pesando {maior}Kg.')
print('As pessoas mais leves foram: ', end='')
for p in princ:
    if p[1] == menor:
        print(f"{p[0]}", end=' ')
print(f'Pesando {menor}Kg.')

