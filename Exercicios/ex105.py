def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)
    if sit == True:
        if r['Média'] < 6:
            return f'{r} Situação: Reprovado'
        elif r['Média'] >= 6:
            return f'{r} Situação: Aprovado'
    return r


#Programa Principal
resp = notas(5.5, 2.5, 8.5, 9, sit=True)
print(resp)