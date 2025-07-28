from datetime import datetime
dados = {}
dados['nome'] = input('Nome: ') #coleta no nome e joga para o dicionario
nascimento = int(input('Ano de Nascimento: ')) #coleta o ano de nascimento 
dados['idade'] = datetime.now().year - nascimento # pega o ano atual e faz o calculo com o ano de nascimento e joga para o dicionario
dados['carteira_trabalho'] = int(input('Carteira de trabalho:     [Digite 0 não tem]  ')) #pergunta se tem carteira de trabalho 

if dados['carteira_trabalho'] != 0: #se tiver carteira de trabalho pergunta abaixo
    dados['ano_contratação'] = int(input('Ano de contratação: ')) #Ano de contratação e joga para o dicionario
    dados['salario'] = float(input('Salário: R$')) # O salario da pessoa e joga para o dicionario
    dados['aposentadoria'] = dados['idade'] + ((dados['ano_contratação'] + 35) - datetime.now().year) #Calcula com qual idade a pessoa vai se aposentar e joga para o dicionario
print('--'*20)
for k,v in dados.items():
    print(f'{k}: {v}')
