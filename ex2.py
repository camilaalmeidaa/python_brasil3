def senha():
    
    user = input("*Exercicio2* Defina o nome de usuario: ")
    senha = input("Exercicio2* Defina a senha: ")
    
    while(user == senha):
        
        print("Erro. A senha não pode ser igual ao usuário. Digite novamente.")
        user = input("*Exercicio2* Defina o nome de usuario: ")
        senha = input("Exercicio2* Defina a senha: ")