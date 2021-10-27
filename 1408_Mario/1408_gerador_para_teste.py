# gera sequencias de 10 armários para teste. qtde_seq é o quanto de sequências que vc deseja
# já joga a string gerada na clipboard. Só dar ctrl+V no arquivo de teste
# Tem um site chamado www.udebug.com que permite a gente testar se os outputs estão batendo

import random
import pyperclip

string = ''
qtde_seq = 100
while qtde_seq > 0:
    qtde_seq -= 1
    tamanho_array = random.randint(1, 10)
    qtde_pedidos = random.randint(1, tamanho_array)
    lista = sorted(random.sample(range(tamanho_array*3), tamanho_array))
    lista = list(map(str, lista))
    str_infos = f'{qtde_pedidos} {tamanho_array}'
    str_lista = ' '.join(lista)
    string = string + "\n" + str_infos + "\n" + str_lista

string += string + "\n0 0"

print(string)
pyperclip.copy(string)