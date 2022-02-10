def taxa_crescimento():
    
    pop_A = 80000
    pop_B = 200000
 
    qtde_anos = 0

    while pop_A <= pop_B:
        pop_A = pop_A + (pop_A * 0.03)
        pop_B = pop_B + (pop_B * 0.015)
        qtde_anos = qtde_anos + 1

    print("A ultrapassa ou iguala a B em",qtde_anos,"anos\n")
    
    
 