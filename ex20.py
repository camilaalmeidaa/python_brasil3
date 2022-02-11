def fatorial2():
    
    num = int(input("*Exercicio20* Digite o numero que deseja saber o fatorial: "))
    
    while(num < 0 or num >= 16):
        
        print("Numero invalido. Digite um numero positivo e menor que 16.")
        num = int(input("Digite o numero que deseja saber o fatorial: "))
        
    fat = 1
    count = 1

    while count <= num: 
        
        fat = fat * count  
        count = count + 1  

    print(fat)
    
