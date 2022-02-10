def fibonacci():
    
    termo = int(input("Digite a quantidade de termos desejada da serie de Fibonacci: "))
    
    t1 = 0
    t2 = 1
    
    print(t1)
    print(t2)
    
    count = 3
    
    while(count <= termo):
        
        t3 = t1 + t2
        
        print(t3)
        
        count = count + 1
        
        t1 = t2
        t2 = t3
        
     