import funções

def existe(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criar(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print("Houve um erro na criação do arquivo.")
    else:
        print(f'Arquivo {nome} criado com sucesso')

def ler(nome):
    try:
        a = open(nome, 'rt')
    except:
        print("Erro em ler o arquivo")
    else:
        funções.cabecalho("PESSOAS CADASTRADAS")
        print(f'{"Nome":<30}{"Idade":>7}')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close

def cadastrarPessoa(nome_arquivo, nome='desconhecido', idade=0):
    try:
        a = open(nome_arquivo, 'at')
    except:
        print("Houve um Erro na abertura do arquivo!")
    else:
        try:
            a.write(f'{nome};{idade}\n') #como aparece no arquivo txt
        except:
            print("Houve um erro na hora de escrever os dados!")
        else:
            print(f'{nome} adicionado com sucesso!')
    