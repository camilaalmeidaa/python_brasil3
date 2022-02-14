def tabuada2():
    
    num = int(input("*Exercicio36* Digite o numero que deseja saber a tabuada: "))
    
    inicio = int(input("*Exercicio36* Digite o numero do inicio da tabuada: "))
    
    fim = int(input("*Exercicio36* Digite o numero do fim da tabuada: "))
    
    print("Montar a tabuada de:",num,"\nComeçar por:",inicio,"\nTerminar por:",fim,"\n\nVou montar a tabuada de",num,"começando em",inicio,"e terminando em",fim,":\n")
    
    for i in range(inicio,fim+1):
        
        result = num * i
        
        print(num,"X",i,"=",result)