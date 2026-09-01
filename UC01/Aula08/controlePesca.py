#ControledePesca_python_ver1.0

MULTA = 4.00
controle = "1"
cont = 1
pescas_dia = []
print("=================================\n")
print("\nBEM VINDO AO CALCULADOR DE PESCA")
print("\n      cadastre os valores       ")
print("\n===============================\n")

#Definindo a Repetição:::
while controle == "1":
    peso_pesca = float(input(f"Digite o Peso da {cont}º pesca (em Kg):"))
    if peso_pesca <= 100:
        print(f"\nPeso dentro do limite: {peso_pesca} - não será aplicado multa!")  
    else:
        valor_multa = multa_pesca(peso_pesca)
        pescas_dia.append(valor_multa)
        print("\nPesca cadastrada com sucesso!")
    cont += 1
    print("\n=========================================") 
    print("\nTecle 1 para: Cadastrar"
    "\nTecle 2 para: Verificar Multas"
    "\nTecle 0 para: Sair"
    )   
    print("\n=========================================")  
    resp = input("\nQual das opções você deseja?\n")



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
#DEFININDO AS FUNÇÕES UTILIZADAS:
def multa_pesca():
