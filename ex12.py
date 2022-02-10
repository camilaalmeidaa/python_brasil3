def tabuada():
    
    num = int(input("Digite um numero de 1 e 10: "))
    
    while(num < 1 or num > 10):
        
        print("Numero invalido. Digite novamente.")
        num = int(input("Digite um numero de 0 e 10: "))
        
    print("Tabuada de",num,":\n")
    
    for i in range(1,11,1):
        
        result = num * i
        print(num,"X",i,"=",result)