def caixa():
    
    lista = []
    soma = 0
    
    prod = float(input("*Exercicio31* Preço do produto: "))
    
    lista.append(prod)
    
    while(prod != 0):
        
        prod = float(input("*Exercicio31* Preço do produto: "))
    
        lista.append(prod)
    
    valor = float(input("*Exercicio31* Digite o valor que o cliente forneceu para pagar: "))
    
    print("Lojas Tabajara\n")        
    
    for i in range(len(lista)):
        
        soma = soma + lista[i]
        
        print("Produto",i+1,": R$",lista[i])
    
    print("Total: R$",soma,"\nDinheiro: R$",valor,"\nTroco: R$",valor-soma,"\n")
    
    
    
    
    
    