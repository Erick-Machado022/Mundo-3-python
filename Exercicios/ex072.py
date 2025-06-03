'''Crie um programa que tenha uma dupla totalmente preenchida 
com uma contagem por extenso, de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20)
e mostrá-lo por extenso.'''

contagem = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez',
            'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte',)
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <=20:
            break
        print('Número inválido, tente novamente:')
    print(f'Você digitou o número {contagem[n]}')

    pergunta = input('você quer continuar? [S/N]').strip().upper()[0]
    if pergunta == 'N':
        break
print('Programa finalizado.')
