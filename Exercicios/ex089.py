from time import sleep
ficha = []
while True:
    nome = str(input('Nome: '))
    n1 = int(input('Nota 1: '))
    n2 = int(input('Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2],media])
    while True:
        resp = str(input('Deseja continuar? ')).strip().upper()[0]
        if resp not in 'SN':
            print('Opção invalida tente S para sim / N para não')
        else:
            break
    if resp == 'N':
        break
print('-='*20)
print(f'{'NO.':<4}{'NOME':<10}{'MÉDIA':>8}')
print('-'*20)
for indice, aluno in enumerate(ficha):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.2f}')
while True:
    print('-'*35)
    opcao = int(input('Mostrar notas de qual aluno?     [999 para finalizar]: '))
    if opcao == 999:
        print('Finalizando programa...')
        break
    if opcao <= len(ficha) - 1:
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')
sleep(1)
print('Programa finalizazdo.')