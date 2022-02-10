def taxa_crescimento2():
    
    pop_A = float(input("*Exercicio5* Digite a população do país A: ")) 
    
    while(pop_A <= 0):
        
        print("Número inválido. Digite novamente.")
        pop_A = float(input("Digite a população do país A: ")) 
        
        
    pop_B = float(input("*Exercicio5* Digite a população do país B: ")) 
    
    while(pop_B <= 0):
        
        print("Número inválido. Digite novamente.")
        pop_B = float(input("Digite a população do país B: ")) 
    
    taxa_crescimento_A = float(input("*Exercicio5* Digite a taxa de crescimento ao ano do país A: "))
    
    while(taxa_crescimento_A <= 0):
        
        print("Número inválido. Digite novamente.")
        taxa_crescimento_A = float(input("Digite a taxa de crescimento ao ano do país A: ")) 
    
    taxa_crescimento_B = float(input("*Exercicio5* Digite a taxa de crescimento ao ano do país B: "))
    
    while(taxa_crescimento_B <= 0):
        
        print("Número inválido. Digite novamente.")
        taxa_crescimento_B = float(input("Digite a taxa de crescimento ao ano do país B: ")) 
 
    qtde_anos = 0

    while pop_A <= pop_B:
        pop_A = pop_A + (pop_A * (taxa_crescimento_A / 100))
        pop_B = pop_B + (pop_B * (taxa_crescimento_B / 100))
        qtde_anos = qtde_anos + 1

    print("A ultrapassa ou iguala a B em",qtde_anos,"anos\n")