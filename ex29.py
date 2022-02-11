def loja():
    
    print("Lojas Quase Dois - Tabela de preços\n")
    
    for i in range(1,51,1):
        
        preco = 1.99 * i
        
        print(i,"- R$",preco)