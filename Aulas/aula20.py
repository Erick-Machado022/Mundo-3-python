def dobra(lista): # Função que dobra os valores de uma lista
    pos = 0 #Inicia a lista na posição 0
    while pos < len(lista): #Enquanto a posição for menor que o tamanho da lista
        lista[pos] *= 2 #Dobra o valor do elemento na posição atual
        pos += 1 #avança para o proximo número da lista


numeros = [2, 5 , 4 ,8 , 4, 2, 6]
dobra(numeros)
print(numeros)