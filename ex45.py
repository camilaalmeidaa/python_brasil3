def nota_prova():
    
    print("*Exercicio45* Professor: ")
    
    lista_respostas = []
    
    nota = 0
    
    for i in range(1,11):
        
        resposta = input("*Exercicio45* Digite o gabarito da questão: ")
        
        lista_respostas.append(resposta)
        
    print("\n*Exercicio45* Aluno: ")
    
    lista_alternativas = []
    
    for i in range(1,11):
        
        alternativa = input("*Exercicio45* Digite a sua alternativa da questão: ")
        
        lista_alternativas.append(alternativa)
        
    for i in range(len(lista_respostas)):
        
        if (lista_respostas[i] == lista_alternativas[i]):
            
            nota = nota + 1
        
    print("\nNota:",nota)