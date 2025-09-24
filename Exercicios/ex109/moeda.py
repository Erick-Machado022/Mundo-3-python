def metade(preço=0, formatado = False):
    res = preço / 2
    return res if formatado is False else moeda(res)

def dobro(preço=0, formatado = False):
    res = preço*2
    return res if formatado == False else moeda(res) #Se formatado for igual a False não retorna nada, se for igual a True retorna moeda(preço)

def aumentar(preço=0, taxa=0, formatado=False):
    res = preço + (preço * (taxa/100))
    return res if formatado == False else moeda(res)

def diminuir(preço=0, taxa=0, formatado=False):
    res = preço - (preço * (taxa/100))
    return res if formatado == False else moeda(res)

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')


