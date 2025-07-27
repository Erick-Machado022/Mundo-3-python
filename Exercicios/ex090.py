alunos = {}
alunos['Nome'] = str(input('nome:'))
alunos['Media'] = float(input(f'Media de {alunos["Nome"]}: '))
print('=-'*20)
print(f' - nome é igual a {alunos["Nome"]}')
print(f' - Média é igual a {alunos["Media"]}')
if alunos['Media'] < 7:
    print(' - situação é igual a reprovado')
else:
    print(' - Situação é igual a aprovado')