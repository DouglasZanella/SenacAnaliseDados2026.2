#codigo cadastro_candidato_python_Ver1.0 
cont= int(input("\nQuantos participantes quer cadastrar? ")) 
Ano_atual = int(input("\nEm que ano está realizando o cadastro (AAAA): ")) 

print("\n=========================================") 
print("\n| SEU CADASTRO:|") 
print("\n=========================================") 

for i in range(cont): 
    print(f"\n{i + 1}º Candidato:") 
    nome_candidato = input("\nDigite o nome do candidato(a): ") 
    nascimento = int(input("Digite o ano de nascimento dele(a): ")) 
    if ((nascimento - Ano_atual) < int(18)): 
        print(f"\nO candidato {nome_candidato} é menor de Idade e não pode participar") 
    else: 
        Tel = input("Digite o Telefone do candidato(apenas numero:") 
        mail = input("Digite o Email do candidato")
        print(f"\nDados do {i+1}º candidato:") 
        print("\n=========================================\n") 
        print(nome_candidato)
        print(Tel)
        print(mail)
  

     

