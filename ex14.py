def par_impar():
    
    n1 = int(input("*Exercicio14* Digite um numero: "))
    n2 = int(input("*Exercicio14* Digite um numero: "))
    n3 = int(input("*Exercicio14* Digite um numero: "))
    n4 = int(input("*Exercicio14* Digite um numero: "))
    n5 = int(input("*Exercicio14* Digite um numero: "))
    n6 = int(input("*Exercicio14* Digite um numero: "))
    n7 = int(input("*Exercicio14* Digite um numero: "))
    n8 = int(input("*Exercicio14* Digite um numero: "))
    n9 = int(input("*Exercicio14* Digite um numero: "))
    n10 = int(input("*Exercicio14* Digite um numero: "))
    
    count_par = 0 
    count_impar = 0
    
    for i in range(n1,n10,1):
        
        if(i % 2 == 0):
            
            count_par = count_par + 1
            
        else:
            
            count_impar = count_impar + 1
    
    
    print("Total de numeros pares:",count_par,"\nTotal de numeros impares:",count_impar,"\n")
            