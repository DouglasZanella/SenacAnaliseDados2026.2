# cont= int(input("\nQuantos participantes quer cadastrar? ")) 
# Ano_atual = int(input("\nEm que ano está realizando o cadastro (AAAA): "))
# candidatos_validos=[] 

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
#         mail = input("Digite o e-mail do candidato:\n")
#         candidato = {'nome':nome_candidato, 'idade':idade, 'telefone':Tel, 'email':mail}
#         candidatos_validos.append(candidato)
#         print("\nCandidato cadastrado com sucesso!")
#     print("\nA lista de candidatos é:")
#     print("\n",candidatos_validos) 

#AQUI TERMINA O QUE FOI PEDIDO ------------------------------------------------------------------------

#Melhoria_cadastro_python_ver1.1  
#UPDATE 

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
        candidato = {'nome':nome_candidato, 'idade':idade, 'telefone':Tel, 'email':mail} 
        candidatos_validos.append(candidato) 
        print("\nCandidato cadastrado com sucesso!") 
  
print("\n=========================================") 
print("| CANDIDATOS VÁLIDOS |") 
print("=========================================") 

if len(candidatos_validos) == 0:#se o tamanho "LEN" da lista está vazio significa que nao tem nada dentro então nao tem candidatos válidos! 
    print("\nNenhum candidato válido foi cadastrado.") 
else: 
    for i in range(len(candidatos_validos)):#aqui percorre novamente a lista para imprimir por ordem(e nao em uma linha apenas pois ele imprimira para cada indice da lista ) 
        candidato = candidatos_validos[i]#aqui mostra o conteudo do indice referente ao que o FOR está lendo 
        print(f"\nCandidato nº {i + 1}")#corrigindo a numeração da lista (pois inicia em 0) 
        print("-----------------------------------------")#esse bloco "chama" cada item do dicionario usando a chave de cada um 
        print(f"Nome: {candidato['nome']}") 
        print(f"Idade: {candidato['idade']} anos") 
        print(f"Telefone: {candidato['telefone'][:5]}-{candidato['telefone'][5:]}") 
        print(f"E-mail: {candidato['email']}") 
        print("-----------------------------------------") 