# HELP: O que não estou conseguindo é tratar o input, creio que isto é o problema para o URI aceitar.
entrada_dados = input().splitlines()

resultado = []

for k in range(len(entrada_dados) - 1):
    infos_pedido = [int(x) for x in entrada_dados[2*k].split()]
    if sum(infos_pedido) == 0:
        break
    lista_armarios = [int(x) for x in entrada_dados[2*k+1].split()]

    i = 0
    j = 0
    lista_qtdes_por_sequencia_buscada = []
    if infos_pedido[1] > 1:
        while i < len(lista_armarios) - 1:
            sequencia_procurada = []
            incremento = 0
            while len(sequencia_procurada) < infos_pedido[0]:
                if lista_armarios[-1] in sequencia_procurada:
                    sequencia_procurada.insert(0, sequencia_procurada[0] - 1)
                else:
                    sequencia_procurada.append(lista_armarios[i] + incremento)
                    incremento += 1
            recorte_lista_armarios = lista_armarios[i:i+infos_pedido[0]]
            i += 1
            dif_listas = len(set(sequencia_procurada) - set(recorte_lista_armarios))
            lista_qtdes_por_sequencia_buscada.append(dif_listas)
        resultado.append(min(lista_qtdes_por_sequencia_buscada))

    else:
        resultado.append(0)

for numero in resultado:
    print(numero)