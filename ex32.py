def fatorial3():
    
    num = int(input("*Exercicio32* Digite o numero que deseja saber o fatorial: "))
    
    fat = 1
    count = 1

    while count <= num: 
        
        fat = fat * count  
        count = count + 1
        
    lista = []
    
    print("Fatorial de: ",num,"\n! =")
    
    for i in range(num):
        
        lista.append(i+1)
    
    nova_lista = list(reversed(lista))
    
    for i in range(len(nova_lista)):
        
        print(nova_lista[i],".")
    
    print("=",fat)
