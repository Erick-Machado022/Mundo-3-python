teste = list()
teste.append('Erick') 
teste.append(40) 
galera = list() 
galera.append(teste[:]) # <- Isso copia os papéis
teste[0] = 'Maria' 
teste[1] = 22 
galera.append(teste[:]) # <- Isso copia os papéis
print(galera) 