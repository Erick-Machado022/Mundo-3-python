'''
Crie um programa que tenha uma tupla única com
nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

lista = ('Lápis', 1.25,
         'Borracha', 1,
         'Apagador', 10, 
         'caneta', 1.75, 
         'Marca Texto', 5.50,
         'Caixa de Giz', 10.99, 
         'Estojo', 15.49,
         'Compasso', 3.99,
         'Mochila', 149.99,
         'Livro', 15.90,)

print('='*40)
print(f'{"Tabela de preços papelaria":^40}')
print('='*40)
for item in range(0, len(lista)):
    if item %2 == 0:
        print(f'{lista[item]:.<30}', end='')
    else:
        print(f'R${lista[item]:>7.2f}')
