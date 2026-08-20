#EXERCICIO DE AULA - CALCULO DE LAMPADAS
'''Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para
iluminar um determinado cômodo de uma residência. Dados de entrada: a potência da
lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do
cômodo. Considere que a potência necessária é de 3 watts por metro quadrado e a cada
3m² existe um bocal para uma lâmpada
'''
'''
#PROGRAMA NA VERSÃO 1.0:
#codigohouse_light_python_Ver1.0 

Largura = float(input("Digite a largura do ambiente (em metros): ")) 
Comprimento = float(input("\nDigite o Comprimento do ambiente(em metros):"))
Potencia_lamp = float(input("\nDigite a potência de suas lâmpadas (em Watts): "))

#calcular a área:  

Area_comodo = (Largura * Comprimento)
#calculo de potencia total 

Potencia_total = (Area_comodo * 3)#potencia total para iluminar todo o ambiente 
 
#Calculo de quantidade de lamapdas necessárias:  

qtd_final = (Potencia_total / Potencia_lamp) 

print(f"\n A quantidade de lâmpadas necessárias para iluminar este ambiente é de : {qtd_final:.0f}")
'''
#codigohouse_light_python_Ver1.1 

Largura = float(input("Digite a largura do ambiente (em metros): "))

Comprimento = float(input("\nDigite o Comprimento do ambiente(em metros):")) 

Potencia_lamp = float(input("\nDigite a potência de suas lâmpadas (em Watts): "))

#calcular a área:  

Area_comodo = (Largura * Comprimento)  

#calculo de potencia total 

Potencia_total = (Area_comodo * 3) #potencia total para iluminar todo o ambiente 
 
#Calculo de quantidade de lamapdas necessárias:  

Qtd_final = (Potencia_total / Potencia_lamp) 

#Calculo de Bocais no ambiente por m² 

Tot_bocal = (Area_comodo / 3) 

#Estrutura condicional para verificar se é possível iluminar com o limitador de quantidade de bocal:  

if Tot_bocal >= Qtd_final: 

    print("================================================================================")

    print(f"\n O Ambiente será totalmente iluminado por um total de {Qtd_final:.0f} Lâmpadas")

    print("\n================================================================================")

else: 

    print("================================================================================")

    print("\nO Ambiente não poderá ser totalmente iluminado")

    print(f"\npois necessita de {Qtd_final:.0f} Lâmpadas de {Potencia_lamp} Watts")

    print(f"\ne o Ambiente só possui {Tot_bocal:.0f} bocais disponíveis")

    print(f"\nRecomenda-se adiquirir lâmpadas com potência maior do que {(Area_comodo*3) / Potencia_lamp} Watts")

    print("================================================================================\n")
