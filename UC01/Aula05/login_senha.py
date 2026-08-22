#codigo_login_senha_python_ver1.1 
#UPDATE 

cont = 0 
while cont < 3:
    login = input("Digite seu nome de usuário: ") 
    senha = input("Digite sua senha:") 
    if (login == "admin" and senha == "admin123"): 
        print(f"\nBem-vindo {login}!") 
        break #encerra aqui o loop 
    else: 
        print("\nVocê Digitou login/senha incorretos, tente novamente:") 
        print(f"\nVocê só possui mais {3 - (cont+1)} tentativas!\n") 
    cont =+ 1