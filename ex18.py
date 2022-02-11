def n_numeros(lista):
    
    soma = 0
    
    for i in range(len(lista)):
        
        soma = soma + lista[i]
    
    print("Maior:",max(lista),"\nMenor:",min(lista),"\nSoma:",soma)
   