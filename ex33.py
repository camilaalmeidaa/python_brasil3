def temperaturas(lista):
    
    soma = 0
    
    maior = 0 
    menor = 1000
    
    for i in range(len(lista)):
        
        soma = soma + lista[i]
            
        if(lista[i] > maior and lista[i] < 1000):
                
            maior = lista[i]
            
        elif(lista[i] < menor):
                
            menor = lista[i]
            
        
        
            
            
    print("Maior:",maior,"\nMenor:",menor,"\nMédia:",soma/len(lista))
    
