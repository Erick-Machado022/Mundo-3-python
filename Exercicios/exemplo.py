frase = input('Digite uma palavra: ').lower()
frase1 = frase.replace(" ", '')
if frase1 == frase1[::-1]:
    print(f'{frase} e {frase1[::-1]} é palindromo')
else:
    print(f'{frase} e {frase1[::-1]} não é palindromo')