teste = list()
teste.append('Erick') #add o nome Erick na lista
teste.append(40) #Add a idade 
galera = list() #geramos a lista galera
galera.append(teste) #demos append na lista do teste
teste[0] = 'Maria' #mudamos o 'Erick' para 'Maria'
teste[1] = 22 # e mudamos de 40 para 22
galera.append(teste) # demos append novamente em teste
print(galera) # Gerou duas listas iguais.