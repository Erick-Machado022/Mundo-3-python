import moeda

preço = float(input('Digite um preço: R$ '))

print(f'A metade de {moeda.moeda(preço)} é {moeda.moeda(moeda.metade(preço))}')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.dobro(preço)}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(preço, 10))}')
