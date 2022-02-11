def cds():
    
    qtde_cds = int(input("*Exercicio28* Digite a quantidade de cds: "))
    
    soma = 0
    
    for i in range(qtde_cds):
        
        valor = float(input("Digite o valor gasto em cada cd: "))
        
        soma = soma + valor
       
      
    media = round(soma / qtde_cds)
    
    print("Total gasto: R$",soma,"\nMedia de gasto por cd: R$",media,"\n")
        
        