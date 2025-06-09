# LISTAS SÃO MUTAVÉIS
num = [2, 5 , 9 , 1]
num[2] = 3
num.append(7) #adiciona o item especificado ao final.
num.sort() # ordena em ordem crescente
num.sort(reverse=True)  #ordena em ordem decrescente
num.insert(2, 0) # Insere uma número em uma posição. 'Na posição 2 insira 0'
#num.pop() # Quando inserido sem índice, elimina o ultimo elemento.
num.remove(2) # Ele procura do inicio da lista até o valor que foi mandado eliminar