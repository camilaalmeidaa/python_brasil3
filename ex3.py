def valida():
    
    nome = input("*Exercicio3* Digite o nome: ")
    
    while(len(nome) <= 3):
        
        print("Nome inválido. Digite um nome com mais de 3 caracteres.")
        nome = input("Digite o nome: ")
        
        
        
    idade = int(input("*Exercicio3* Digite a idade: "))
    
    while(idade < 0 or idade > 150):
        
        print("Idade inválida. Digite uma idade entre 0 e 150.")
        idade = int(input("Digite a idade: "))
    
    
    
    salario = float(input("*Exercicio3* Digite o salário: "))
    
    while(salario <= 0):
        
        print("Salario inválido. Digite um salario maior que 0.")
        salario = float(input("Digite o salário: "))
        
        
        
    sexo = input("*Exercicio3* Digite o sexo 'f' - feminino ou 'm' - masculino: ")
    
    while(sexo != 'f' and sexo != 'm'):
        
        print("Sexp inválido. Digite novamente.")
        sexo = input("Digite o sexo 'f' - feminino ou 'm' - masculino: ")
        
        
    estado_civil = input("*Exercicio3* Digite o estado civil 's' - solteiro(a), 'c' - casado(a), 'v' - viúvo(a) ou 'd' - divorciado(a): ")
    
    while(estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd'):
        
        print("Estado civil inválido. Digite novamente.")
        estado_civil = input("Digite o estado civil 's' - solteiro(a), 'c' - casado(a), 'v' - viúvo(a) ou 'd' - divorciado(a): ")
