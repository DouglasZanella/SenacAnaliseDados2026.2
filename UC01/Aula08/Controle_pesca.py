#ControledePesca_python_ver1.1 
#TYPEERROR_FIX 

MULTA = 4.00 
LIMITE_PESO = 100 
#controle do while (começa "TRUE") 
controle = "1" 
  
#definindo as funções::  
def multa_pesca(peso_pesca): 
    if peso_pesca <= LIMITE_PESO: 
        return 0 
    else: 
        excesso = peso_pesca - LIMITE_PESO 
        valor_multa = excesso * MULTA 
        return valor_multa 

  #definindo uma lista para armazenar o hitórico(consultas futuras)  
historico_pesca = [] 
total_multas = 0 

print("=================================") 
print(" BEM-VINDO AO CALCULADOR DE PESCA") 
print("=================================") 

#enquanto o usuário nao apertar 0 para sair:  
while controle != "0": 
    #se o usuário escolher "1"ele cadastra:  
    if controle == "1": 
        peso = float( 
            input("\nDigite o peso da pesca ou 0 para sair: ") 
        ) 
        #esse If serve apenas para "sair" pois a pesca foi "zero" ou seja nenhuma:  
        if peso == 0: 
            break 
        #chama a função com o valor do peso digitado   
        multa = multa_pesca(peso) 
        #criar um dicionario com as informações para incluir lá na lista criada de histórico  
        pesca = { 
            "peso": peso, 
            "multa": multa 
        } 
        #adiciona o dicionario de pesca lá na lista:          
        historico_pesca.append(pesca) 
        #controle do somatório: total de multas:  
        total_multas += multa 
        #se a pesca tiver multa informar ao usuário  
        if multa > 0: 
            print("\nEssa pesca possui multa a pagar!") 
            print(f"Valor da multa: R$ {multa:.2f}") 
        #senao, só segue  
        else: 
            print("\nPesca dentro do limite.") 
            print("Não possui multa a pagar!") 

    #se o usuário digirou 2 para ver como está o histórico até o momento:  
    elif controle == "2": 
        print("\n========== HISTÓRICO DAS PESCARIAS ==========") 
        #se o "tamanho" daquela lista lá atrás for 0 então nao tem nada cadastrado  
        if len(historico_pesca) == 0: 
            print("\nNenhuma pescaria foi registrada.") 
        #senão, vamos entrar num loop para cada elemento da lista  
        else: 
            for i in range(len(historico_pesca)): 
                pesca = historico_pesca[i] 
                print(f"\nPescaria nº {i + 1}") 
                print("---------------------------------------------") 
                print(f"Peso: {pesca['peso']:.2f} kg") 
                print(f"Multa: R$ {pesca['multa']:.2f}") 

            print("\n=============================================") 
            print( 
                f"Quantidade de pescarias: " 
                f"{len(historico_pesca)}" 
            ) 
            print( 
                f"Total de multas acumuladas: " 
                f"R$ {total_multas:.2f}" 
            ) 

    else: 
        print("\nOpção inválida!") 
    #verifica novamente o que o usuário quer antes de sair  
    print("\n=========================================") 
    print("Tecle 1 para: Novo cadastro") 
    print("Tecle 2 para: Histórico de multas") 
    print("Tecle 0 para: Sair") 
    print("=========================================")

    controle = input("\nQual das opções você deseja? ") 

print("\nObrigado por usar o programa de controle de pescas!") 