 #TUPLAS SÃO IMUTÁVEIS
# TUPLAS SÃO REPRESENTADAS POR PARENTESES ()

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1]) # Mostra o item na posição 1: 'Suco'

print(lanche[1:3]) # Mostra do índice 1 até 2: ('Suco', 'Pizza')

print(lanche[2:]) # Mostra o elemento 2 até o final ('Pizza', 'Pudim')

print(lanche[:2]) # Mostra do início até o índice 1:  ('Hambúrguer', 'Suco')

 # índices negativos contam de trás para frente:
print(lanche[-2]) # Mostra o penúltimo item: 'Pizza'

print(sorted(lanche)) # Mostre o Lanche em ordem 



for comida in lanche:
    print(f'Eu vou comer {comida}') 
print('Comi muito!') 

'''
O for percorre automaticamente todos os itens da tupla lanche.
A cada volta, imprime: "Eu vou comer [item]".
Depois que termina, imprime: "Comi muito!".
'''

a = (2, 5, 4)
b = (5, 8 , 1, 2)
c = a + b #Tuplas podem ser concatenadas com +.
print(sorted(c))  #Para ordenar, usamos sorted(), que devolve uma lista ordenada.