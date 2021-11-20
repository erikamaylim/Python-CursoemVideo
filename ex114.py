"""Crie um código em Python que teste se o site pudim está acessível pelo computador usado."""
from uteis.cores import RED, GREEN, END
import requests

try:
    site = requests.get("http://pudim.com.br/")
except:
    print(f'{RED}OPS!{END} O site está fora do ar. ')
else:
    print(f'{GREEN}LEGAL!{END} O site está funcionando.')
