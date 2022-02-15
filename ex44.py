def votacao():
    
    
    print("1 - José\n2- João\n3- Pedro\n4- Carlos\n5- Voto Nulo\n6- Voto em Branco\n")
    
    lista = []
    
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    
    voto = int(input("*Exercicio44* Digite seu voto: "))
    
    lista.append(voto)
    
    while(voto != 0):
        
        voto = int(input("*Exercicio44* Digite seu voto: "))
    
        lista.append(voto)
    
    for i in range(len(lista)):
        
        if lista[i] == 1:
            
            count1 = count1 + 1
        
        elif lista[i] == 2:
            
            count2 = count2 + 1
        
        elif lista[i] == 3:
            
            count3 = count3 + 1
        
        elif lista[i] == 4:
            
            count4 = count4 + 1
        
        elif lista[i] == 5:
            
            count5 = count5 + 1
        
        elif lista[i] == 6:
            
            count6 = count6 + 1
            
    total = count1 + count2 + count3 + count4 + count5 + count6
        
    print("\nJosé:",count1,"votos\nJoão:",count2,"votos\nPedro:",count3,"votos\nCarlos:",count4,"votos\nVotos Nulos:",count5,"votos\nVotos em Branco:",count6,"votos\n")
    
    print(round((count5 / total) * 100),"% de votos nulos")
    print(round((count6 / total) * 100),"% de votos em branco")
    
        
        
    
    