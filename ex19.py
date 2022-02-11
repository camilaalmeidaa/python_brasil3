def n_numeros2(lista):
    
    soma = 0
    
    maior = 0 
    menor = 1000
    
    for i in range(len(lista)):
        
        if(lista[i] > 0 and lista[i] < 1000):
        
            soma = soma + lista[i]
            
            if(lista[i] > maior and lista[i] < 1000):
                
                maior = lista[i]
            
            if(lista[i] < menor):
                
                menor = lista[i]
            
        
        elif(lista[i] <= 0 or lista[i] >= 1000):
            
            print("Só são validos numeros entre 1 e 1000\n")
            
            
    print("Maior:",maior,"\nMenor:",menor,"\nSoma:",soma)
        
   