'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas 
posições na lista.'''

lista = []

for c in range (0, 5):
        lista.append(int(input(f'Digite um valor para a posição {c}: ')))
maior = max(lista)
menor = min(lista)
print(f'O maior valor digitado foi {maior} na posição ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {menor} na posição ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end='')

