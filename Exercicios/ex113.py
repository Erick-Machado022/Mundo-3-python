def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("ERRO! o valor, digite um valor inteiro valido")
            continue
        except (KeyboardInterrupt):
            print("\nO usuario preferiu não digitar este valor")
            return 0
        else:
            return n 

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO! por favor informe um número real valido.')
            continue
        else:
            return n

num = leiaInt("Digite um valor inteiro: ")
num2 = leiaFloat("Digite um valor real: ")
print(f"O valor inteiro digitado foi {num} e o real foi {num2}")