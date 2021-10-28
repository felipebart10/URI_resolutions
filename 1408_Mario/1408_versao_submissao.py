# HELP: O que não estou conseguindo é tratar o input, creio que isto é o problema para o URI aceitar.
while True:
    infos_pedido = list(map(int, input().split()))
    if sum(infos_pedido) == 0:
        break
    lista_armarios = list(map(int, input().split()))
    i = 0
    j = 0
    
    lista_qtdes_por_sequencia_buscada = []
    while i < len(lista_armarios) - 1:
        sequencia_procurada = list(map(lambda x: x+lista_armarios[i], list(range(infos_pedido[0]))))
        recorte_lista_armarios = lista_armarios[i:i+infos_pedido[0]]
        i += 1
        dif_listas = len(set(sequencia_procurada) - set(recorte_lista_armarios))
        lista_qtdes_por_sequencia_buscada.append(dif_listas)
    if len(lista_armarios) == 1:
        resultado = 0
    else:
        resultado = min(lista_qtdes_por_sequencia_buscada)
    print(resultado)