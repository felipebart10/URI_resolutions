"""
    EXPLICANDO A LÓGICA:
    O Input é um texto multi-linha, sendo a primeira linha com os dados do pedido do cliente e a qtde em estoque.
    A Segunda linha é a sequência da numeração de armários existente
    O primeiro elemento na linha dos dados do pedido é a quantidade de caixas que o cliente quer, portanto é a sequência que queremos montar.
    Com este valor, eu irei montar diversos subsets para cada item da lista_armario e comparar este sub-set com a sequência desejada para aquela posição
    Segue exemplo abaixo para maior compreensão. Tem algumas linhas de print para debug, apenas remova o comentário delas.
"""

# INPUT
texto = """2 6
1 3 4 5 6 8
0 0"""

entrada_dados = texto.splitlines()

resultado = []

# Loop para separar cada uma das linhas do input
for k in range(len(entrada_dados) - 1):
    infos_pedido = [int(x) for x in entrada_dados[2*k].split()]
    # Se for a linha '0 0' ele para
    if sum(infos_pedido) == 0:
        break
    lista_armarios = [int(x) for x in entrada_dados[2*k+1].split()]

    i = 0
    j = 0
    lista_qtdes_por_sequencia_buscada = []
    # Se o tamanho da lista de armário for maior que 1, faz o processo
    if infos_pedido[1] > 1:

        # Esse loop obtém o sub-set para cada posição
        while i < len(lista_armarios) - 1:
            sequencia_procurada = []
            incremento = 0

            # Esse loop defina a sequência a ser procurada
            while len(sequencia_procurada) < infos_pedido[0]:
                if lista_armarios[-1] in sequencia_procurada:
                    sequencia_procurada.insert(0, sequencia_procurada[0] - 1)
                else:
                    sequencia_procurada.append(lista_armarios[i] + incremento)
                    incremento += 1

            # Aqui retorna o sub-set a partir da posição i
            recorte_lista_armarios = lista_armarios[i:i+infos_pedido[0]]
            i += 1

            # Aqui é feita a comparação da lista procurada com o sub-set. Essa diferença é a qtde de trocas necessária
            dif_listas = len(set(sequencia_procurada) - set(recorte_lista_armarios))
            lista_qtdes_por_sequencia_buscada.append(dif_listas)

            # PRINTS PARA DEBUG:
            #print(f'seq procurada: {sequencia_procurada}')
            #print(f'seq sub-set: {recorte_lista_armarios}')
            #print(f'trocas necessárias: {dif_listas}')
            #print()

        # Aqui é obtido a menor qtde de trocas necessárias dentre todas as comparações feitas
        resultado.append(min(lista_qtdes_por_sequencia_buscada))


    # Se o tamanho da lista for 1, retorna o resultado 0
    else:
        resultado.append(0)

# Printa todos os resultados calculados
for numero in resultado:
    print(numero)
    