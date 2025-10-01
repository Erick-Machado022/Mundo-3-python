import funções
import arquivo
from time import sleep



nome_arquivo = "MenuPython.txt"

if arquivo.existe(nome_arquivo):
    print("Arquivo encontrado")
else:
    print("Arquivo não existe")
    arquivo.criar(nome_arquivo)

while True:
    resposta = funções.menu(["Ver pessoas cadastradas","Cadastrar nova Pessoa","Sair do Sistema"])
    
    if resposta == 1:
        #Listar o conteúdo do arquivo
        arquivo.ler(nome_arquivo)
    elif resposta == 2:
        #CADASTRAR nova pessoa
        funções.cabecalho('NOVO CADASTRO')
        nome = input("Nome: ")
        idade = funções.leiaInt("Idade:")
        arquivo.cadastrarPessoa(nome_arquivo, nome, idade)
        
    elif resposta == 3:
        #Sair do programa
        funções.cabecalho("Finalizando Programa... Volte sempre ")
        break
    else:
        print("\033[31mERRO! Digite uma opção válida\033[m")
    sleep(2)
