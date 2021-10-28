def getLargestSubsequenceSize(my_vector, k):
    max_count = 0
    i = 0
    j = 0
    soma = 0
    
    while j < len(my_vector):
        soma += my_vector[j]
        if soma > k:
            curr_count = j - i
            if curr_count > max_count:
                max_count = curr_count
            soma -= my_vector[i]
            i += 1
        j += 1
    
    if j - i > max_count:
        return j - i + 1
    else:
        return max_count + 1

def main():
    while True:
        infos_pedido = list(map(int, input().split()))
        if sum(infos_pedido) == 0:
            break
        lista_armarios = list(map(int, input().split()))

        diferencas = []
        
        for i in range(len(lista_armarios) - 1):
            diferencas.insert(0, lista_armarios[i+1] - lista_armarios[i])
        
        print(infos_pedido[0] - getLargestSubsequenceSize(diferencas, infos_pedido[0] - 1))
    
    return 0

main()

    
