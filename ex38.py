def salario():
    
    salario = float(input("*Exercicio38* Digite o salário inicial do funcionário em 1995: "))
    ano = 1995
    ano_atual = int(input("*Exercicio38* Digite em que ano estamos: "))
    
    aumento = 0.015

    while ano < ano_atual:
        
        ano = ano + 1
        salario = salario * (1 + aumento)
        aumento = aumento * 2

    print(f"O salario em {ano} é de R$ {salario:.2f}")