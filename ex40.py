def acidentes():
    
    soma_veiculos = 0
    soma_acidentes = 0
    
    lista_cod = []
    lista_veiculos = []
    lista_acidentes = []
    
    for i in range(5):
        
        cod = input("*Exercicio40* Digite o código da cidade: ")
        num_veiculos = int(input("*Exercicio40* Digite o numero de veiculos de passeio (em 1999): "))
        num_acidentes = int(input("*Exercicio40* Digite o numero de acidentes de transito com vitimas (em 1999): "))
    
        lista_cod.append(cod)
        lista_veiculos.append(num_veiculos)
        lista_acidentes.append(num_acidentes)
        
        soma_veiculos = soma_veiculos + lista_veiculos[i]
        soma_acidentes = soma_acidentes + lista_acidentes[i]
        
    
  

    print("Maior indice de acidentes:",max(lista_acidentes),"\nMenor indice de acidentes:",min(lista_acidentes),"\nMedia de veiculos:",soma_veiculos/len(lista_veiculos),"\nMedia de acidentes:",soma_acidentes/len(lista_acidentes),"\n")
    
    
    
