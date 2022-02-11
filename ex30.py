def loja2():
    
    preco_pao = float(input("*Exercicio30* Digite o preco do pao: "))
    
    for i in range(1,51,1):
        
        preco = preco_pao * i
        
        print(i,"- R$",preco)