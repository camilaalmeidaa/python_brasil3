def primo3():
    
    num = int(input("*Exercicio34* Digite um numero inteiro: "))
    
    nao_primo = 0
  
    
    for i in range(2,num-1,1):
        
        if(num % i == 0):
            
            nao_primo = 1
            
        
    if(nao_primo == 1):
        
        print("Numero nao é primo.\n")
    
    else:
        
        print("Numero é primo\n")