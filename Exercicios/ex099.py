def maior(*num):
    contador = maior = 0  # Inicializa contador e maior com zero
    print('-='*20)
    print('Análisando valores...')
    
    for valor in num: # Percorre cada número recebido
        print(f'{valor} ', end='') #Os números informados
        
        if contador == 0: #Se o contador for 0 
            maior = valor #O maior número é o valor (0)
        else: 
            if valor > maior: #Se o valor for maior que o maior anterior
                maior = valor #O maior passa a ser o valor
        contador += 1 #ele passa cada número informado
    print(f"Foram informados {contador} valores ao todo")
    print(f"O maior número foi {maior}.")
    print('-='*20)

    
maior(2, 9, 4, 5, 7, 1)
maior(3,5,4)
maior(8, 5, 4, 7, 7, 9, 9)
maior()
maior(5)