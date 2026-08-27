#Melhoria_cadastro_python_ver1.3 

#UPDATE 

Ano_atual = int(input("\nInforme o ano em que está realizando o cadastro(somente números ex.:AAAA):")) 
candidatos_validos=[] 
cont = 1 
resp = "1"

print("\n===============================================") 
print(f"\n| BEM-VINDO AO CADASTRO DE CANDIDATOS {Ano_atual}:|")
print("\n===============================================")   
#BLOCO DESNECESSÁRIO:::::::::::::::::::::::::::::::::::::::::::::::::::
# resp = input(str("\nQual das opções você deseja?\n"))
# if resp == "2":
#             print("NENHUM CANDIDATO CADASTRADO!")
#             print("\n=========================================") 
#             print("\nTecle 1 para: Cadastrar"
#             "\nTecle 0 para: Sair"
#             )   
#             print("\n=========================================")     
#             resp = input(str("\nQual das opções você deseja?\n"))
#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
while resp == "1":
        print("\n=========================================")    
        print(f"\n{cont}º Candidato:")   
        nome_candidato= input("\nDigite o nome do candidato(a): ") 
        nascimento = int(input("Digite o ano de nascimento dele(a): "))   
        idade = Ano_atual - nascimento  
        if ( idade < 18):   
            print(f"\nO candidato {nome_candidato} é menor de Idade,{idade} anos, e não pode participar") 
        else:  
            Tel = input("Digite o Telefone do candidato(apenas numero):")   
            mail = input("Digite o e-mail do candidato:\n")  
            candidato = {'nome':nome_candidato, 'idade':idade, 'telefone':Tel, 'email':mail}  
            candidatos_validos.append(candidato)  
            print("\nCandidato cadastrado com sucesso!")  
        
        print("\n=========================================") 
        print("\nTecle 1 para: Cadastrar"
        "\nTecle 2 para: Verificar Cadastro"
        "\nTecle 0 para: Sair"
        )   
        print("\n=========================================")  
        resp = input("\nQual das opções você deseja?")
        cont= cont+1 
        #--------------------------------RESPOSTA NEGATIVA ---------------------------------------
        if resp == "2":
            while resp == "2":
                print("\n=========================================") 
                print("|           CANDIDATOS VÁLIDOS           |") 
                print("===========================================") 
                
                if len(candidatos_validos) == 0: 
                    print("\nNenhum candidato válido foi cadastrado.") 
                else: 
                    for i in range(len(candidatos_validos)): 
                        candidato = candidatos_validos[i] 
                        print(f"\nCandidato nº {i + 1}") 
                        print("-----------------------------------------") 
                        print(f"Nome: {candidato['nome']}")  
                        print(f"Idade: {candidato['idade']} anos")  
                        print(f"Telefone: {candidato['telefone'][:5]}-{candidato['telefone'][5:]}")  
                        print(f"E-mail: {candidato['email']}")  
                        print("-----------------------------------------")
                print("\n=========================================") 
                print("\nTecle 1 para: Cadastrar"
                    "\nTecle 2 para: Verificar Cadastro"
                    "\nTecle 0 para: Sair"
                    )   
                resp = input("\nQual das opções você deseja?\n")

print("OBRIGADO POR USAR O CADASTRO ")





  