import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://dentistaalexandremonteiro.com.br/') #Tenta abrir a URL informada (acessar o site)
except:
    print('O site não está acessível')
else:
    print('O site está ok')