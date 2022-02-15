def juros():
    
    divida = float(input("*Exercicio41* Digite o valor da divida: "))
    
    print("Valor da Dívida\tValor dos Juros\tQuantidade de Parcelas\tValor da Parcela\n",divida,"\t\t 0\t\t\t1\t",divida,"\n",divida+(divida*0.1),"\t\t",divida*0.1,"\t\t\t3\t",(divida+(divida*0.1)/3),"\n",divida+(divida*0.15),"\t\t",divida*0.15,"\t\t\t6\t",(divida+(divida*0.15)/6),"\n",divida+(divida*0.2),"\t\t",divida*0.2,"\t\t\t9\t",(divida+(divida*0.2)/9),"\n",divida+(divida*0.25),"\t\t",divida*0.25,"\t\t\t12\t",(divida+(divida*0.25)/12))
    
    