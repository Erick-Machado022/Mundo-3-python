from time import sleep


def contador (i, f, p):
    if p < 0:
        p *= -1 # Se o passo for negativo, transforma em positivo
    
    if p == 0:
        p = 1 # Se o passo for zero, define como 1 (para evitar erro no range)

    if i < f: # Se o início for menor que o fim, faz uma contagem crescente
        for c in range(i, f + 1, p):
            print(c, end=' ')
            sleep(0.3)
    else:  # Se o início for maior que o fim, faz uma contagem decrescente
        for c in range(i, f - 1, -p):
            print(c, end=' ')
            sleep(0.3)
    print('Fim')

def linha():
    print('-='*20)


linha()
print('contador de 1 até 10 de 1 em 1')
contador(1, 10, 1)

linha()
print('contador de 10 ate 0 pulando de 2 em 2')
contador(10, -1, -2)

linha()
print('Agora é sua vez de definir a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
linha()
print('programa finalizado')