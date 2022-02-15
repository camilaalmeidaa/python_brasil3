def pedido():
    
    lista_cod = []
    lista_qtde = []
    
    cod = int(input("*Exercicio43* Digite o codigo do pedido (digite 0 para encerrar): "))
    qtde = int(input("Exercicio43* Digite a quantidade: "))
    
    lista_cod.append(cod)
    lista_qtde.append(qtde)
    
    while(cod != 0):
        
        cod = int(input("*Exercicio43* Digite o codigo do pedido (digite 0 para encerrar): "))
        qtde = int(input("Exercicio43* Digite a quantidade: "))
        
        lista_cod.append(cod)
        lista_qtde.append(qtde)
    
    for i in range(len(lista_cod)):
        
        if(lista_cod[i] == 100):
            
            preco = 1.2 * (lista_qtde[i])
        
        elif(lista_cod[i] == 101):
            
            preco = preco + (1.3 * (lista_qtde[i]))
        
        elif(lista_cod[i] == 102):
            
            preco = preco + (1.5 * (lista_qtde[i]))
        
        elif(lista_cod[i] == 103):
            
            preco = preco + (1.2 * (lista_qtde[i]))
        
        elif(lista_cod[i] == 104):
            
            preco = preco + (1.3 * (lista_qtde[i]))
        
        elif(lista_cod[i] == 105):
            
            preco = preco + lista_qtde[i]
    
    
    print("Valor total: R$",preco)
            
            
            