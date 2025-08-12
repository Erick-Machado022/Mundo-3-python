def voto(ano):
    from datetime import date #Importa a biblioteca datetime para vefificar o ano atual.
    atual = date.today().year #Pega o ano atual
    idade = atual - ano #Pega o ano atual menos o ano de nascimento.
    if idade < 16: #Se a idade for menor que 16
        return f'Com  {idade} anos NÃO VOTA'
    elif 16 <= idade <18 or idade > 65: #Se a idade for 16/17 ou maior que 65 voto opcional
        return f'Com {idade} anos o voto é OPCIONAL'
    else: #Idade maior que 18 voto obrigatório.
        return f'Com {idade} anos o voto é OBRIGATORIO'

nascimento = int(input('Em que ano você naceu?'))
print(voto(nascimento))