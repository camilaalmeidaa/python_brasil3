def academia():
    
    codigo = input("*Exercicio37* Digite o codigo: ")
    altura = float(input("*Exercicio37* Digite a altura: "))
    peso = float(input("*Exercicio37* Digite o peso: "))
    
    lista_codigos = []
    lista_alturas = []
    lista_pesos = []
    
    soma_alturas = 0
    soma_pesos = 0
    
    lista_codigos.append(codigo)
    lista_alturas.append(altura)
    lista_pesos.append(peso)
    
    while(codigo != 0):
        
        codigo = int(input("*Exercicio37* Digite o codigo: "))
        altura = float(input("*Exercicio37* Digite a altura: "))
        peso = float(input("*Exercicio37* Digite o peso: "))
        
        lista_codigos.append(codigo)
        
        if(altura > 0 and peso > 0):
            
            lista_alturas.append(altura)
            lista_pesos.append(peso)
        
    
    for i in range(len(lista_alturas)):
        
        soma_alturas = soma_alturas + lista_alturas[i]
        
    for j in range(len(lista_pesos)):
        
        soma_pesos = soma_pesos + lista_pesos[j]


    media_alturas = round(soma_alturas / len(lista_alturas))
    media_pesos = round(soma_pesos / len(lista_pesos))
    
    print("Mais alto:",max(lista_alturas),"\nMais baixo:",min(lista_alturas),"\nMais gordo:",max(lista_pesos),"\nMais magro:",min(lista_pesos),"\nMedia alturas:",media_alturas,"m\nMedia pesos:",media_pesos,"kg\n")
        