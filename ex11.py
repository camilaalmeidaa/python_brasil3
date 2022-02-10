def intervalo2():
    
    n1 = int(input("*Exercicio10* Digite um numero inteiro: "))
    n2 = int(input("*Exercicio10* Digite um numero inteiro: "))
    
    soma = 0
    
    for count in range(n1+1,n2,1):
        
        print(count)
        soma = soma + count
    
    print("A soma é:",soma,"\n")