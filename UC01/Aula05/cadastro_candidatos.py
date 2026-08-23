#codigo_cadastro_candidatos_python_ver1.0 
# cont= 12 
# Ano_atual = 2026 

# print("\n=========================================") 
# print("\n| SEU CADASTRO:|") 
# print("\n=========================================") 
 

# for i in range(cont): 

#     print(f"\n{i + 1}º Candidato:") 
#     nome_candidato= input("\nDigite o nome do candidato(a): ") 
#     nascimento = int(input("Digite o ano de nascimento dele(a): ")) 
#     idade = Ano_atual - nascimento 

#     if ( idade < 18): 
#         print(f"\nO candidato {nome_candidato} é menor de Idade,{idade} anos, e não pode participar") 

#     else: 
#         Tel = input("Digite o Telefone do candidato(apenas numero:") 
#         mail = input("Digite o e-mail do candidato:") 
#         print(f"\nDados do {i+1}º candidato:") 
#         print("\n=========================================") 
#         print(f"Nome: {nome_candidato}") 
#         print(f"Idade: {idade}") 
#         print(f"Telefone: {Tel}")        
#         print(f"Email: {mail}")       

#AQUI TERMINA O QUE FOI PEDIDO   
#---------------------------------------------------------------------------------------------------------

#codigo cadastro_candidato_python_Ver1.2 
#UPDATE 
cont= int(input("\nQuantos participantes quer cadastrar? ")) 
Ano_atual = int(input("\nEm que ano está realizando o cadastro (AAAA): ")) 
print("\n=========================================") 
print("\n| SEU CADASTRO:|") 
print("\n=========================================") 

  
for i in range(cont): 
    print(f"\n{i + 1}º Candidato:") 
    nome_candidato= input("\nDigite o nome do candidato(a): ") 
    nascimento = int(input("Digite o ano de nascimento dele(a): ")) 
    idade = Ano_atual - nascimento 
    if ( idade < 18): 
        print(f"\nO candidato {nome_candidato} é menor de Idade,{idade} anos, e não pode participar") 
    else:
        Tel = input("Digite o Telefone do candidato(apenas numeros):") 
        mail = input("Digite o e-mail do candidato:\n") 
        print("--------------DADOS--------------") 
        print(f"Nome: {nome_candidato}") 
        print(f"Idade: {idade}") 
        print(f"Telefone: {Tel[:5]}-{Tel[5:]}")#aqui a função do "[:5] é pegar tudo na  variavel ate a posição 5 sem incluir a posição 5 
        print(f"Email: {mail}") 
        print("\n--------------FIM--------------") 