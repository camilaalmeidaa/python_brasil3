def nota_prova():
    
    print("*Exercicio45* Professor: ")
    
    lista_respostas = []
    lista_alternativas = []
    lista_notas = []
    
    nota = 0
    qtde_alunos = 1
    
    for i in range(1,11):
        
        resposta = input("*Exercicio45* Digite o gabarito da questão: ")
        
        lista_respostas.append(resposta)
        
    print("\n*Exercicio45* Aluno: ")
    
    
    for i in range(1,11):
        
        alternativa = input("*Exercicio45* Digite a sua alternativa da questão: ")
        
        lista_alternativas.append(alternativa)
        
    for i in range(len(lista_respostas)):
        
        if (lista_respostas[i] == lista_alternativas[i]):
            
            nota = nota + 1
            lista_notas.append(nota)
            
    aluno = input("\nOutro aluno vai utilizar o sistema [s/n]: ")
    
    if(aluno == 's'):
        
        qtde_alunos = qtde_alunos + 1
        
        for i in range(1,11):
        
            alternativa = input("*Exercicio45* Digite a sua alternativa da questão: ")
        
            lista_alternativas.append(alternativa)
        
        for i in range(len(lista_respostas)):
        
            if (lista_respostas[i] == lista_alternativas[i]):
            
                nota = nota + 1
                lista_notas.append(nota)
        
        soma = 0
                
        for i in range(len(lista_notas)):
        
            soma = soma + lista_notas[i]
        
        media = soma / qtde_alunos
    
        aluno = input("\nOutro aluno vai utilizar o sistema [s/n]: ")
    

    elif(aluno == 'n'):
        
        print("\nMaior nota:",max(lista_notas),"\nMenor nota:",min(lista_notas),"\nTotal de alunos que utilizaram o sistema:",qtde_alunos,"\nMedia da turma:",media,"\n")
    
    