def primo4():
    
    num = int(input("*Exercicio35* Digite um numero: ")) 
    

    for count in range(1, num + 1):
        
        if count > 1:
            
            for i in range(2, count):
                
                if (count % i) == 0:
                    
                    break
                
            else:
                    
                print(count)
   
        
        