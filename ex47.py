def ginasta():
    
    lista = []
 
    nome = input("*Exercicio47* Digite o nome do atleta: ")
    
    for i in range(7):
        
        salto = float(input("*Exercicio46* Digite a nota: "))
        
        lista.append(salto)
    
    
        
    print("\nAtleta:",nome)
            
    for i in range(len(lista)):
        
        print("Nota:",lista[i])
        
    print("Resultado Final:\n")
    print("Atleta:",nome,"\nMaior nota:",max(lista),"\nMenor nota:",min(lista))
    
    lista.remove(max(lista))
    lista.remove(min(lista))
    
    media = sum(lista) / len(lista)
    
    print("Media:",media,"\n")
    
        
        
       
        
        
        
    
    