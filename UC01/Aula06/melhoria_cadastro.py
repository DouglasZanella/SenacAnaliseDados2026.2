cont= int(input("\nQuantos participantes quer cadastrar? ")) 
Ano_atual = int(input("\nEm que ano está realizando o cadastro (AAAA): "))
candidatos_validos=[] 

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
        Tel = input("Digite o Telefone do candidato(apenas numero:") 
        mail = input("Digite o e-mail do candidato:\n")
        candidato = {'nome':nome_candidato, 'telefone':Tel, 'email':mail}
        candidatos_validos.append(candidato)

        # print("--------------DADOS--------------") 
        # print(f"Nome: {nome_candidato}") 
        # print(f"Idade: {idade}") 
        # print(f"Telefone: {Tel[:5]}-{Tel[5:]}")#aqui a função do "[:5] é pegar tudo na  variavel ate a posição 5 sem incluir a posição 5 
        # print(f"Email: {mail}") 
        # print("--------------FIM--------------") 
print("\nA lista de candidatos é:") 
for candidator in candidatos_validos: 
    print("\n",candidatos_validos)