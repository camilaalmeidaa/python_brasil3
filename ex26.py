def eleicao():
    
    num_eleitores = int(input("*Exercicio26* Digite o numero total de eleitores: "))
    
    count_A = 0
    count_B = 0
    count_C = 0
    
    for i in range(num_eleitores):
        
        voto = input("Digite em qual candidato voce deseja votar ('A', 'B' ou 'C'): ")
        
        if(voto == 'A' or voto == 'a'):
            
            count_A = count_A + 1
        
        elif(voto == 'B' or voto == 'b'):
            
            count_B = count_B + 1
        
        elif(voto == 'C' or voto == 'c'):
            
            count_C = count_C + 1
            
    
    print("Candidato A:",count_A,"votos\nCandidato B:",count_B,"votos\nCandidato C:",count_C,"votos\n")



