def media_alunos():
    
    qtde_turmas = int(input("*Exercicio27* Digite a quantidade de turmas: "))
    
    lista = []
    
    for i in range(qtde_turmas):
        
        qtde_alunos = int(input("Digite a quantidade de alunos na turma: "))
        
        
        if(qtde_alunos <= 40):
            
            lista.append(qtde_alunos)
            
        elif(qtde_alunos > 40):
            
            print("Numero invalido. Turma nao pode ter mais de 40 alunos.")
            qtde_alunos = int(input("Digite a quantidade de alunos na turma: "))
 
    
    soma = 0 
    
    for count in range(len(lista)):
        
        soma = soma + lista[count]
        
    
    media = soma / qtde_turmas
    
    print("A media de alunos por turma é",media)