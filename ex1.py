def pede_nota():
    
    nota = float(input("*Exercicio1* Digite uma nota entre 0 e 10: "))
    
 
    while(nota < 0 or nota > 10):
        
        print("Nota Inválida. Digite novamente.")
        nota = float(input("*Exercicio1* Digite uma nota entre 0 e 10: "))
    