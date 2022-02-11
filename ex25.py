def media_idades(lista):
    
    soma = 0 
    
    for i in range(len(lista)):
        
        soma = soma + lista[i]
    
    media = round(soma / len(lista))
    
    if(media >= 60):
        
        print("Media:",media,"anos - Idosa\n")
    
    elif(media > 25):
        
        print("Media:",media,"anos - Adulta\n")
        
    else:
        
        print("Media:",media,"anos - Jovem\n")
        
        

