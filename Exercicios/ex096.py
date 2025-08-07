def area(larg, comp):
    a = largura * Comprimento
    print(f'A area de um terreno {larg}x{comp} é {a}m²')

print('Controle de Terrenos')
print('-'*20)
largura = float(input('Largura (m):'))
Comprimento = float(input('Comprimento (m): '))
area(largura,Comprimento)