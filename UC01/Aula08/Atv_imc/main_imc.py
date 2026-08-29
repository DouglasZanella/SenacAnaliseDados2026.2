#Main_IMC_ver1.0
#programa principal do IMC

from calculo_imc import calc_imc
from classificacao_imc import classificacao

pessoas_cadastradas=[]
controle ="1"
contador=1

while controle !="0":
    if controle == "1":
        nome_pessoa = input("Digite o nome de usuário: ")
        peso = float(input("Digite seu Peso(em Kg): "))
        altura = float(input("Digite sua altura (em m): "))
        imc_pessoa = calc_imc(peso,altura)
        classificacao_pessoa = classificacao(imc_pessoa)
        
        dados_pessoa = {
            'nome':nome_pessoa,
            'peso':peso,
            'altura':altura,
            'imc':imc_pessoa,
            'classificacao':classificacao_pessoa
        }

        pessoas_cadastradas.append(dados_pessoa)
        print("IMC cadastrado com Sucesso! \n")

    elif controle == "2":
        print("\n========== HISTÓRICO ==========")
        for i in range(len(pessoas_cadastradas)): 
            dados_finais = pessoas_cadastradas[i] 
            print(f"\n{i + 1}º Pessoa cadastrada:") 
            print("---------------------------------------------") 
            print(f"\nNome da pessoa: {dados_finais['nome']}")
            print(f"\nPeso: {dados_finais['peso']:.2f} kg")
            print(f"\nAltura: {dados_finais['altura']:.2f} m")
            print(f"\nIMC: {dados_finais['imc']:.2f} Kg/m²")
            print(f"\nVocê está: {dados_finais['classificacao']}")
    else: 
        print("\nOpção inválida!")

    print("\n=========================================") 
    print("Tecle 1 para: Novo cadastro") 
    print("Tecle 2 para: Histórico") 
    print("Tecle 0 para: Sair") 
    print("\n=========================================")
    controle = input("\nQual das opções você deseja? \n")

print("\nObrigado por Usar o cadastro de IMC" )

