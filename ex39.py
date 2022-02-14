def alunos(lista):
    
    lista_invertida = []
    
    for i in range(len(lista)):
        
        tupla_invertida = lista[i][::-1]
        
        lista_invertida.append(tupla_invertida)
        

    print("Mais alto:",max(lista_invertida),"\nMais baixo:",min(lista_invertida),"\n")
    